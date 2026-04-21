from flask import Blueprint, jsonify, request, current_app
from backend.db_connection import get_db
from mysql.connector import Error

admin = Blueprint("admin", __name__)


# ------------------------------------------------------------
# 1. POST /admin/players
# User Story 4.1 - Add new player to the system so they
# can see their account and stats.
# ------------------------------------------------------------
@admin.route("/players", methods=["POST"])
def add_player():
    cursor = get_db().cursor(dictionary=True)
    try:
        data = request.get_json()
        required = ["username", "region", "join_date"]
        for field in required:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        cursor.execute("""
            INSERT INTO Player
                (username, region, join_date, current_rank,
                 current_rank_points, total_matches,
                 current_win_rate, overall_accuracy,
                 team_id, rank_tier_id, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    CURDATE(), CURDATE())
        """, (
            data["username"],
            data["region"],
            data["join_date"],
            data.get("current_rank", "Bronze"),
            data.get("current_rank_points", 0),
            data.get("total_matches", 0),
            data.get("current_win_rate", 0.0),
            data.get("overall_accuracy", 0.0),
            data.get("team_id"),
            data.get("rank_tier_id")
        ))
        get_db().commit()
        return jsonify({"message": "Player added",
                        "player_id": cursor.lastrowid}), 201
    except Error as e:
        current_app.logger.error(f"Error in add_player: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


# ------------------------------------------------------------
# 2. PUT /admin/players/<player_id>
# User Story 4.2 - Update existing player info to correct
# any incorrect data.
# ------------------------------------------------------------
@admin.route("/players/<int:player_id>", methods=["PUT"])
def update_player(player_id):
    cursor = get_db().cursor(dictionary=True)
    try:
        data = request.get_json()
        allowed = [
            "username", "region", "current_rank",
            "current_rank_points", "total_matches",
            "current_win_rate", "overall_accuracy",
            "team_id", "rank_tier_id"
        ]
        updates = [f"{f} = %s" for f in allowed if f in data]
        params  = [data[f] for f in allowed if f in data]

        if not updates:
            return jsonify({"error": "No valid fields to update"}), 400

        updates.append("updated_at = CURDATE()")
        params.append(player_id)
        cursor.execute(
            f"UPDATE Player SET {', '.join(updates)} WHERE player_id = %s",
            params
        )
        get_db().commit()
        if cursor.rowcount == 0:
            return jsonify({"error": "Player not found"}), 404
        return jsonify({"message": "Player updated"}), 200
    except Error as e:
        current_app.logger.error(f"Error in update_player: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


# ------------------------------------------------------------
# 3. POST /admin/data-sources
# User Story 4.3 - Add new data sources so the app can
# support new features as the game evolves.
# ------------------------------------------------------------
@admin.route("/data-sources", methods=["POST"])
def add_data_source():
    cursor = get_db().cursor(dictionary=True)
    try:
        data = request.get_json()
        required = ["source_name", "source_type", "api_endpoint"]
        for field in required:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        cursor.execute("""
            INSERT INTO DataSource
                (source_name, source_type, api_endpoint, status, added_date)
            VALUES (%s, %s, %s, %s, CURDATE())
        """, (
            data["source_name"],
            data["source_type"],
            data["api_endpoint"],
            data.get("status", "active")
        ))
        get_db().commit()
        return jsonify({"message": "Data source added",
                        "source_id": cursor.lastrowid}), 201
    except Error as e:
        current_app.logger.error(f"Error in add_data_source: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


# ------------------------------------------------------------
# 4. GET /admin/audit-flags
# User Story 4.4 - View match records flagged for impossible
# stats to identify potential cheaters.
# ------------------------------------------------------------
@admin.route("/audit-flags", methods=["GET"])
def get_audit_flags():
    cursor = get_db().cursor(dictionary=True)
    try:
        status_filter = request.args.get("status")
        query = """
            SELECT
                af.audit_flag_id,
                af.flag_type,
                af.flag_reason,
                af.flag_date,
                af.review_status,
                p.username,
                pmp.accuracy_pct,
                pmp.damage,
                pmp.kills
            FROM AuditFlag af
            JOIN PlayerMatchPerformance pmp
                ON af.performance_id = pmp.performance_id
            JOIN Player p ON pmp.player_id = p.player_id
            WHERE 1=1
        """
        params = []
        if status_filter:
            query += " AND af.review_status = %s"
            params.append(status_filter)
        query += " ORDER BY af.flag_date DESC"
        cursor.execute(query, params)
        return jsonify(cursor.fetchall()), 200
    except Error as e:
        current_app.logger.error(f"Error in get_audit_flags: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


# ------------------------------------------------------------
# 5. PUT /admin/audit-flags/<flag_id>
# User Story 4.4 - Update the review status of an audit flag
# (e.g. clear a flag or mark as confirmed cheat).
# ------------------------------------------------------------
@admin.route("/audit-flags/<int:flag_id>", methods=["PUT"])
def update_audit_flag(flag_id):
    cursor = get_db().cursor(dictionary=True)
    try:
        data = request.get_json()
        if "review_status" not in data:
            return jsonify({"error": "Missing required field: review_status"}), 400

        cursor.execute("""
            UPDATE AuditFlag
            SET review_status = %s
            WHERE audit_flag_id = %s
        """, (data["review_status"], flag_id))
        get_db().commit()
        if cursor.rowcount == 0:
            return jsonify({"error": "Audit flag not found"}), 404
        return jsonify({"message": "Audit flag updated"}), 200
    except Error as e:
        current_app.logger.error(f"Error in update_audit_flag: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


# ------------------------------------------------------------
# 6. POST /admin/archive-season
# User Story 4.5 - Archive match data from a previous season
# so current season queries run faster.
# ------------------------------------------------------------
@admin.route("/archive-season", methods=["POST"])
def archive_season():
    cursor = get_db().cursor(dictionary=True)
    try:
        data = request.get_json()
        if "season_name" not in data:
            return jsonify({"error": "Missing required field: season_name"}), 400

        season = data["season_name"]

        # Insert into ArchivedMatch
        cursor.execute("""
            INSERT INTO ArchivedMatch
                (original_match_id, season_name, match_date, archived_date)
            SELECT match_id, season_name, match_date, CURDATE()
            FROM `Match`
            WHERE season_name = %s
        """, (season,))
        archived_count = cursor.rowcount

        get_db().commit()
        return jsonify({
            "message": f"Season '{season}' archived successfully",
            "matches_archived": archived_count
        }), 201
    except Error as e:
        current_app.logger.error(f"Error in archive_season: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


# ------------------------------------------------------------
# 7. GET /admin/reports
# User Story 4.6 - Generate reports on weapon usage,
# location trends, and data usage.
# ------------------------------------------------------------
@admin.route("/reports", methods=["GET"])
def get_reports():
    cursor = get_db().cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT
                m.map_name,
                m.mode,
                COUNT(pmp.performance_id) AS total_performances,
                AVG(pmp.kills)            AS avg_kills,
                AVG(pmp.damage)           AS avg_damage,
                AVG(pmp.accuracy_pct)     AS avg_accuracy
            FROM `Match` m
            JOIN PlayerMatchPerformance pmp ON m.match_id = pmp.match_id
            GROUP BY m.map_name, m.mode
            ORDER BY total_performances DESC
        """)
        return jsonify(cursor.fetchall()), 200
    except Error as e:
        current_app.logger.error(f"Error in get_reports: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


# ------------------------------------------------------------
# 8. GET /admin/players
# Get all players for admin management view.
# ------------------------------------------------------------
@admin.route("/players", methods=["GET"])
def get_all_players():
    cursor = get_db().cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT
                p.player_id, p.username, p.region,
                p.current_rank, p.current_rank_points,
                p.total_matches, t.team_name
            FROM Player p
            LEFT JOIN Team t ON p.team_id = t.team_id
            ORDER BY p.username ASC
        """)
        return jsonify(cursor.fetchall()), 200
    except Error as e:
        current_app.logger.error(f"Error in get_all_players: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


# ------------------------------------------------------------
# 9. GET /admin/data-sources
# View all registered data sources.
# ------------------------------------------------------------
@admin.route("/data-sources", methods=["GET"])
def get_data_sources():
    cursor = get_db().cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM DataSource ORDER BY added_date DESC")
        return jsonify(cursor.fetchall()), 200
    except Error as e:
        current_app.logger.error(f"Error in get_data_sources: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


# ------------------------------------------------------------
# 10. DELETE /admin/players/<player_id>
# User Story 4.4 - Remove a confirmed cheating account.
# ------------------------------------------------------------
@admin.route("/players/<int:player_id>", methods=["DELETE"])
def delete_player(player_id):
    cursor = get_db().cursor(dictionary=True)
    try:
        cursor.execute(
            "DELETE FROM Player WHERE player_id = %s", (player_id,)
        )
        get_db().commit()
        if cursor.rowcount == 0:
            return jsonify({"error": "Player not found"}), 404
        return jsonify({"message": "Player deleted"}), 200
    except Error as e:
        current_app.logger.error(f"Error in delete_player: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()

# 11. POST /admin/matches
# Add a new match record to the system
@admin.route("/matches", methods=["POST"])
def add_match():
    cursor = get_db().cursor(dictionary=True)
    try:
        data = request.get_json()
        required = ["match_date", "season_name", "map_name", "mode"]
        for field in required:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
 
        cursor.execute("""
            INSERT INTO `Match`
                (match_date, season_name, map_name, mode,
                 match_duration, tournament_name, source_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            data["match_date"],
            data["season_name"],
            data["map_name"],
            data["mode"],
            data.get("match_duration"),
            data.get("tournament_name"),
            data.get("source_id")
        ))
        get_db().commit()
        return jsonify({"message": "Match added",
                        "match_id": cursor.lastrowid}), 201
    except Error as e:
        current_app.logger.error(f"Error in add_match: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()

# 12. POST /admin/matches/<match_id>/performance
# Add a palyer performance record to a specific match
@admin.route("/matches/<int:match_id>/performance", methods=["POST"])
def add_match_performance(match_id):
    cursor = get_db().cursor(dictionary=True)
    try:
        data = request.get_json()
        required = ["player_id", "kills", "deaths", "assists",
                    "damage", "placement", "accuracy_pct"]
        for field in required:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
 
        cursor.execute("""
            INSERT INTO PlayerMatchPerformance
                (player_id, match_id, legend_id, weapon_id,
                 kills, deaths, assists, damage,
                 placement, knockdowns, accuracy_pct, win_flag,
                 is_included_in_analysis, is_active)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, TRUE, TRUE)
        """, (
            data["player_id"],
            match_id,
            data.get("legend_id"),
            data.get("weapon_id"),
            data["kills"],
            data["deaths"],
            data["assists"],
            data["damage"],
            data["placement"],
            data.get("knockdowns", 0),
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


# 13. POST /admin/legends
# Add a new legend to the game
@admin.route("/legends", methods=["POST"])
def add_legend():
    cursor = get_db().cursor(dictionary=True)
    try:
        data = request.get_json()
        required = ["legend_name", "class_type"]
        for field in required:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
 
        cursor.execute("""
            INSERT INTO Legend (legend_name, class_type)
            VALUES (%s, %s)
        """, (data["legend_name"], data["class_type"]))
        get_db().commit()
        return jsonify({"message": "Legend added",
                        "legend_id": cursor.lastrowid}), 201
    except Error as e:
        current_app.logger.error(f"Error in add_legend: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()

# 14. POST /admin/weapons
# Add a new weapon to the game
@admin.route("/weapons", methods=["POST"])
def add_weapon():
    cursor = get_db().cursor(dictionary=True)
    try:
        data = request.get_json()
        required = ["weapon_name", "weapon_type", "ammo_type"]
        for field in required:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
 
        cursor.execute("""
            INSERT INTO Weapon (weapon_name, weapon_type, ammo_type)
            VALUES (%s, %s, %s)
        """, (data["weapon_name"], data["weapon_type"], data["ammo_type"]))
        get_db().commit()
        return jsonify({"message": "Weapon added",
                        "weapon_id": cursor.lastrowid}), 201
    except Error as e:
        current_app.logger.error(f"Error in add_weapon: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()