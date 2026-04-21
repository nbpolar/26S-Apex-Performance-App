from flask import Blueprint, jsonify, request, current_app
from backend.db_connection import get_db
from mysql.connector import Error

coach = Blueprint("coach", __name__)


# ------------------------------------------------------------
# 1. GET /coach/team-compositions
# User Story 1.1 - View usage rates for popular competitive
# team compositions to determine the most effective comp.
# ------------------------------------------------------------
@coach.route("/team-compositions", methods=["GET"])
def get_team_compositions():
    cursor = get_db().cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT
                l1.legend_name AS legend_1,
                l2.legend_name AS legend_2,
                l3.legend_name AS legend_3,
                COUNT(*) AS times_used
            FROM TeamComposition tc
            JOIN Legend l1 ON tc.legend_1 = l1.legend_id
            JOIN Legend l2 ON tc.legend_2 = l2.legend_id
            JOIN Legend l3 ON tc.legend_3 = l3.legend_id
            GROUP BY l1.legend_name, l2.legend_name, l3.legend_name
            ORDER BY times_used DESC
        """)
        return jsonify(cursor.fetchall()), 200
    except Error as e:
        current_app.logger.error(f"Error in get_team_compositions: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


# ------------------------------------------------------------
# 2. GET /coach/teams/<team_id>/death-heatmap
# User Story 1.2 - View heatmap of player death locations
# to advise team on which areas to avoid.
# ------------------------------------------------------------
@coach.route("/teams/<int:team_id>/death-heatmap", methods=["GET"])
def get_death_heatmap(team_id):
    cursor = get_db().cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT
                ml.location_name,
                ml.x_coord,
                ml.y_coord,
                ml.map_name,
                COUNT(*) AS death_count
            FROM PlayerMatchPerformance pmp
            JOIN MapLocation ml ON pmp.death_location_id = ml.location_id
            JOIN Player p ON p.player_id = pmp.player_id
            WHERE p.team_id = %s
            GROUP BY ml.location_name, ml.x_coord, ml.y_coord, ml.map_name
            ORDER BY death_count DESC
        """, (team_id,))
        return jsonify(cursor.fetchall()), 200
    except Error as e:
        current_app.logger.error(f"Error in get_death_heatmap: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


# ------------------------------------------------------------
# 3. GET /coach/teams/<team_id>/placement-vs-kills
# User Story 1.3 - View placement vs kills/damage to identify
# if the meta favors aggressive or passive playstyle.
# ------------------------------------------------------------
@coach.route("/teams/<int:team_id>/placement-vs-kills", methods=["GET"])
def get_placement_vs_kills(team_id):
    cursor = get_db().cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT
                pmp.placement,
                AVG(pmp.kills)  AS avg_kills,
                AVG(pmp.damage) AS avg_damage,
                COUNT(*)        AS match_count
            FROM PlayerMatchPerformance pmp
            JOIN Player p ON p.player_id = pmp.player_id
            WHERE p.team_id = %s
            GROUP BY pmp.placement
            ORDER BY pmp.placement ASC
        """, (team_id,))
        return jsonify(cursor.fetchall()), 200
    except Error as e:
        current_app.logger.error(f"Error in get_placement_vs_kills: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


# ------------------------------------------------------------
# 4. GET /coach/teams/<team_id>/damage-to-kills
# User Story 1.4 - View player damage to kill ratios to
# identify if players are struggling to finish gunfights.
# ------------------------------------------------------------
@coach.route("/teams/<int:team_id>/damage-to-kills", methods=["GET"])
def get_damage_to_kills(team_id):
    cursor = get_db().cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT
                p.username,
                SUM(pmp.damage)     AS total_damage,
                SUM(pmp.kills)      AS total_kills,
                SUM(pmp.knockdowns) AS total_knockdowns
            FROM PlayerMatchPerformance pmp
            JOIN Player p ON p.player_id = pmp.player_id
            WHERE p.team_id = %s
            GROUP BY p.username
            ORDER BY total_damage DESC
        """, (team_id,))
        return jsonify(cursor.fetchall()), 200
    except Error as e:
        current_app.logger.error(f"Error in get_damage_to_kills: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


# ------------------------------------------------------------
# 5. GET /coach/players/<player_id>/accuracy-by-weapon
# User Story 1.5 - View player accuracy by weapon type to
# recommend fitting weapon loadouts.
# ------------------------------------------------------------
@coach.route("/players/<int:player_id>/accuracy-by-weapon", methods=["GET"])
def get_accuracy_by_weapon(player_id):
    cursor = get_db().cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT
                p.username,
                w.weapon_type,
                w.weapon_name,
                AVG(pmp.accuracy_pct) AS avg_accuracy
            FROM PlayerMatchPerformance pmp
            JOIN Player p  ON p.player_id  = pmp.player_id
            JOIN Weapon w  ON w.weapon_id   = pmp.weapon_id
            WHERE p.player_id = %s
            GROUP BY p.username, w.weapon_type, w.weapon_name
            ORDER BY avg_accuracy DESC
        """, (player_id,))
        return jsonify(cursor.fetchall()), 200
    except Error as e:
        current_app.logger.error(f"Error in get_accuracy_by_weapon: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


# ------------------------------------------------------------
# 6. GET /coach/teams/<team_id>/knockdown-efficiency
# User Story 1.6 - Compare damage to knockdowns to identify
# players securing meaningful frags vs poke damage.
# ------------------------------------------------------------
@coach.route("/teams/<int:team_id>/knockdown-efficiency", methods=["GET"])
def get_knockdown_efficiency(team_id):
    cursor = get_db().cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT
                p.username,
                SUM(pmp.damage)     AS total_damage,
                SUM(pmp.knockdowns) AS total_knockdowns,
                ROUND(SUM(pmp.damage) / NULLIF(SUM(pmp.knockdowns), 0), 2)
                    AS damage_per_knockdown
            FROM PlayerMatchPerformance pmp
            JOIN Player p ON p.player_id = pmp.player_id
            WHERE p.team_id = %s
            GROUP BY p.username
            ORDER BY damage_per_knockdown ASC
        """, (team_id,))
        return jsonify(cursor.fetchall()), 200
    except Error as e:
        current_app.logger.error(f"Error in get_knockdown_efficiency: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


# ------------------------------------------------------------
# 7. GET /coach/teams
# Get all teams (for coach to browse/select a team)
# ------------------------------------------------------------
@coach.route("/teams", methods=["GET"])
def get_all_teams():
    cursor = get_db().cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Team ORDER BY team_name ASC")
        return jsonify(cursor.fetchall()), 200
    except Error as e:
        current_app.logger.error(f"Error in get_all_teams: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


# ------------------------------------------------------------
# 8. POST /coach/team-compositions
# Add a new team composition record for a match.
# ------------------------------------------------------------
@coach.route("/team-compositions", methods=["POST"])
def add_team_composition():
    cursor = get_db().cursor(dictionary=True)
    try:
        data = request.get_json()
        required = ["match_id", "team_id", "legend_1", "legend_2", "legend_3"]
        for field in required:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        cursor.execute("""
            INSERT INTO TeamComposition (match_id, team_id, legend_1, legend_2, legend_3)
            VALUES (%s, %s, %s, %s, %s)
        """, (data["match_id"], data["team_id"],
              data["legend_1"], data["legend_2"], data["legend_3"]))
        get_db().commit()
        return jsonify({"message": "Team composition added",
                        "composition_id": cursor.lastrowid}), 201
    except Error as e:
        current_app.logger.error(f"Error in add_team_composition: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


# ------------------------------------------------------------
# 9. PUT /coach/team-compositions/<composition_id>
# Update legends in an existing team composition.
# ------------------------------------------------------------
@coach.route("/team-compositions/<int:composition_id>", methods=["PUT"])
def update_team_composition(composition_id):
    cursor = get_db().cursor(dictionary=True)
    try:
        data = request.get_json()
        allowed = ["legend_1", "legend_2", "legend_3"]
        updates = [f"{f} = %s" for f in allowed if f in data]
        params  = [data[f] for f in allowed if f in data]

        if not updates:
            return jsonify({"error": "No valid fields to update"}), 400

        params.append(composition_id)
        cursor.execute(
            f"UPDATE TeamComposition SET {', '.join(updates)} WHERE composition_id = %s",
            params
        )
        get_db().commit()
        return jsonify({"message": "Team composition updated"}), 200
    except Error as e:
        current_app.logger.error(f"Error in update_team_composition: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


# ------------------------------------------------------------
# 10. DELETE /coach/team-compositions/<composition_id>
# Remove a team composition record.
# ------------------------------------------------------------
@coach.route("/team-compositions/<int:composition_id>", methods=["DELETE"])
def delete_team_composition(composition_id):
    cursor = get_db().cursor(dictionary=True)
    try:
        cursor.execute(
            "DELETE FROM TeamComposition WHERE composition_id = %s",
            (composition_id,)
        )
        get_db().commit()
        if cursor.rowcount == 0:
            return jsonify({"error": "Composition not found"}), 404
        return jsonify({"message": "Team composition deleted"}), 200
    except Error as e:
        current_app.logger.error(f"Error in delete_team_composition: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
