from flask import Blueprint, jsonify, request, current_app
from backend.db_connection import get_db
from mysql.connector import Error

admin = Blueprint("admin", __name__)


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
