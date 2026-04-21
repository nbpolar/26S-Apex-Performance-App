from flask import Blueprint, jsonify, request, current_app
from backend.db_connection import get_db
from mysql.connector import Error

competitive = Blueprint("competitive", __name__)


@competitive.route("/players/<int:player_id>/performance", methods=["GET"])
def get_player_performance(player_id):
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

@competitive.route("/players/<int:player_id>/performance-history", methods=["GET"])
def get_performance_history(player_id):
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


@competitive.route("/leaderboard", methods=["GET"])
def get_leaderboard():
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


@competitive.route("/meta/trends", methods=["GET"])
def get_meta_trends():
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


@competitive.route("/players/<int:player_id>/match-history", methods=["GET"])
def get_match_history(player_id):
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

@competitive.route("/players/<int:player_id>/weapon-stats", methods=["GET"])
def get_player_weapon_stats(player_id):
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
)
def exclude_match(player_id, performance_id):
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
)
def include_match(player_id, performance_id):
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


@competitive.route("/players/<int:player_id>", methods=["GET"])
def get_player_profile(player_id):
    cursor = get_db().cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT
                p.player_id,
                p.username,
                p.region,
                p.join_date,
                p.current_rank,
                p.current_rank_points,
                p.current_rank_position,
                p.total_matches,
                p.current_win_rate,
                p.overall_accuracy,
                t.team_name,
                rt.tier_name,
                rt.division_name
            FROM Player p
            LEFT JOIN Team     t  ON p.team_id      = t.team_id
            LEFT JOIN RankTier rt ON p.rank_tier_id = rt.rank_tier_id
            WHERE p.player_id = %s
        """, (player_id,))
        result = cursor.fetchone()
        if not result:
            return jsonify({"error": "Player not found"}), 404
        return jsonify(result), 200
    except Error as e:
        current_app.logger.error(f"Error in get_player_profile: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
 
