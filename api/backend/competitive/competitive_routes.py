from flask import  Blueprint, jsonify, request, current_app
from backend.db_connection import get_db
from mysql.connector import Error

competitive = Blueprint("competitive", __name__)


@competitive.route("/players/<int:player_id>/performance", methods=["GET"])  # type: ignore[misc]
def get_player_performance(player_id : int)
    """Accesses player performance"""
    cursor = get_db().cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT
                p.username,
                SUM(pmp.kills)  AS total_kills,
                AVG(pmp.accuracy_pct) AS average_accuracy,
                ROUND(
                    COUNT(CASE WHEN pmp.placement = 1 THEN 1 END) * 100.0
                    / COUNT(*), 2
                ) AS win_percentage
            FROM Player p
            JOIN PlayerMatchPerformance pmp ON p.player_id = pmp.player_id
            WHERE p.player_id = %s
              AND pmp.is_included_in_analysis = TRUE
            GROUP BY p.username
        """, (player_id,))
        result = cursor.fetchone()
        if not result:
            return jsonify({"error": "Player not found"}), 404
        return jsonify(result), 200
    except Error as e:
        current_app.logger.error(f"Error in get_player_performance: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


@competitive.route("/players/<int:player_id>/performance-history", methods=["GET"]) # type: ignore[misc]
def get_performance_history(player_id : int)
    """Accesses player performance history"""
    cursor = get_db().cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT
                m.match_date,
                pmp.kills,
                pmp.damage,
                pmp.accuracy_pct,
                pmp.placement
            FROM PlayerMatchPerformance pmp
            JOIN `Match` m ON pmp.match_id = m.match_id
            WHERE pmp.player_id = %s
              AND pmp.is_included_in_analysis = TRUE
            ORDER BY m.match_date ASC
        """, (player_id,))
        return jsonify(cursor.fetchall()), 200
    except Error as e:
        current_app.logger.error(f"Error in get_performance_history: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


@competitive.route("/leaderboard", methods=["GET"]) # type: ignore[misc]
def get_leaderboard()
    """Accesses leaderboard"""
    cursor = get_db().cursor(dictionary=True)
    try:
        limit = request.args.get("limit", 20, type=int)
        cursor.execute("""
            SELECT
                p.username,
                p.current_rank_points,
                p.current_rank_position,
                rt.tier_name,
                rt.division_name
            FROM Player p
            JOIN RankTier rt ON p.rank_tier_id = rt.rank_tier_id
            ORDER BY p.current_rank_points DESC
            LIMIT %s
        """, (limit,))
        return jsonify(cursor.fetchall()), 200
    except Error as e:
        current_app.logger.error(f"Error in get_leaderboard: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


@competitive.route("/meta/trends", methods=["GET"]) # type: ignore[misc]
def get_meta_trends()
    """Accesses trends in the meta"""
    cursor = get_db().cursor(dictionary=True)
    try:
        season = request.args.get("season")
        query = """
            SELECT
                mt.season_name,
                mt.patch_version,
                l.legend_name,
                w.weapon_name,
                mt.usage_rate,
                mt.win_rate,
                mt.pick_rate,
                mt.trend_date
            FROM MetaTrend mt
            LEFT JOIN Legend l ON mt.legend_id = l.legend_id
            LEFT JOIN Weapon w ON mt.weapon_id  = w.weapon_id
            WHERE 1=1
        """
        params = []
        if season:
            query += " AND mt.season_name = %s"
            params.append(season)
        query += " ORDER BY mt.win_rate DESC"
        cursor.execute(query, params)
        return jsonify(cursor.fetchall()), 200
    except Error as e:
        current_app.logger.error(f"Error in get_meta_trends: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


@competitive.route("/players/<int:player_id>/match-history", methods=["GET"]) # type: ignore[misc]
def get_match_history(player_id : int)
    """Accesses match history"""
    cursor = get_db().cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT
                pmp.performance_id,
                m.match_id,
                m.match_date,
                m.map_name,
                m.mode,
                pmp.kills,
                pmp.placement,
                pmp.damage,
                pmp.is_included_in_analysis
            FROM PlayerMatchPerformance pmp
            JOIN `Match` m ON pmp.match_id = m.match_id
            WHERE pmp.player_id = %s
            ORDER BY m.match_date DESC
        """, (player_id,))
        return jsonify(cursor.fetchall()), 200
    except Error as e:
        current_app.logger.error(f"Error in get_match_history: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


@competitive.route("/players/<int:player_id>/weapon-stats", methods=["GET"]) # type: ignore[misc]
def get_player_weapon_stats(player_id : int)
    """Accesses weapon stats per player"""
    cursor = get_db().cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT
                w.weapon_name,
                w.weapon_type,
                pwp.total_kills,
                pwp.avg_damage,
                pwp.avg_accuracy_pct,
                pwp.kd_ratio,
                pwp.matches_used
            FROM PlayerWeaponPerformance pwp
            JOIN Weapon w ON pwp.weapon_id = w.weapon_id
            WHERE pwp.player_id = %s
            ORDER BY pwp.kd_ratio DESC
        """, (player_id,))
        return jsonify(cursor.fetchall()), 200
    except Error as e:
        current_app.logger.error(f"Error in get_player_weapon_stats: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


@competitive.route(
    "/players/<int:player_id>/matches/<int:performance_id>/exclude",
    methods=["PUT"]
) # type: ignore[misc]
def exclude_match(player_id : int, performance_id : int)
    """Excludes a player match"""
    cursor = get_db().cursor(dictionary=True)
    try:
        cursor.execute("""
            UPDATE PlayerMatchPerformance
            SET is_included_in_analysis = FALSE
            WHERE performance_id = %s AND player_id = %s
        """, (performance_id, player_id))
        get_db().commit()
        if cursor.rowcount == 0:
            return jsonify({"error": "Match performance record not found"}), 404
        return jsonify({"message": "Match excluded from analysis"}), 200
    except Error as e:
        current_app.logger.error(f"Error in exclude_match: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


@competitive.route(
    "/players/<int:player_id>/matches/<int:performance_id>/include",
    methods=["PUT"]
) # type: ignore[misc]
def include_match(player_id : int, performance_id : int)
    """Includes a player match"""
    cursor = get_db().cursor(dictionary=True)
    try:
        cursor.execute("""
            UPDATE PlayerMatchPerformance
            SET is_included_in_analysis = TRUE
            WHERE performance_id = %s AND player_id = %s
        """, (performance_id, player_id))
        get_db().commit()
        if cursor.rowcount == 0:
            return jsonify({"error": "Match performance record not found"}), 404
        return jsonify({"message": "Match included in analysis"}), 200
    except Error as e:
        current_app.logger.error(f"Error in include_match: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


@competitive.route("/players/<int:player_id>/performance", methods=["POST"]) # type: ignore[misc]
def add_match_performance(player_id : int)
    """Adds a player's match performance"""
    cursor = get_db().cursor(dictionary=True)
    try:
        data = request.get_json()
        required = ["match_id", "kills", "deaths", "assists",
                    "damage", "placement", "accuracy_pct"]
        for field in required:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        cursor.execute("""
            INSERT INTO PlayerMatchPerformance
                (player_id, match_id, kills, deaths, assists, damage,
                 placement, accuracy_pct, win_flag,
                 is_included_in_analysis, is_active)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s,
                    %s, TRUE, TRUE)
        """, (
            player_id,
            data["match_id"],
            data["kills"],
            data["deaths"],
            data["assists"],
            data["damage"],
            data["placement"],
            data["accuracy_pct"],
            data.get("win_flag", False)
        ))
        get_db().commit()
        return jsonify({"message": "Performance record added",
                        "performance_id": cursor.lastrowid}), 201
    except Error as e:
        current_app.logger.error(f"Error in add_match_performance: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
