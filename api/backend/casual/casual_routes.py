from flask import Blueprint, jsonify, request, current_app, ResponseReturnValue
from backend.db_connection import get_db
from mysql.connector import Error

casual = Blueprint("casual", __name__)


@casual.route("/meta/top-weapons", methods=["GET"]) # type: ignore[misc]
def get_top_weapons() -> ResponseReturnValue:
    """Accesses top weapons"""
    cursor = get_db().cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT
                w.weapon_name,
                w.weapon_type,
                AVG(pwp.kd_ratio) AS avg_kd
            FROM PlayerWeaponPerformance pwp
            JOIN Weapon w ON pwp.weapon_id = w.weapon_id
            GROUP BY w.weapon_name, w.weapon_type
            ORDER BY avg_kd DESC
            LIMIT 10
        """)
        return jsonify(cursor.fetchall()), 200
    except Error as e:
        current_app.logger.error(f"Error in get_top_weapons: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()

@casual.route("/meta/top-legends", methods=["GET"]) # type: ignore[misc]
def get_top_legends() -> ResponseReturnValue:
    """Accesses top legends"""
    cursor = get_db().cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT
                l.legend_name,
                l.class_type,
                AVG(plp.win_rate) AS avg_win_rate,
                AVG(plp.kd_ratio) AS avg_kd
            FROM PlayerLegendPerformance plp
            JOIN Legend l ON plp.legend_id = l.legend_id
            GROUP BY l.legend_name, l.class_type
            ORDER BY avg_win_rate DESC
            LIMIT 10
        """)
        return jsonify(cursor.fetchall()), 200
    except Error as e:
        current_app.logger.error(f"Error in get_top_legends: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


@casual.route("/players/<int:player_id>/stats", methods=["GET"]) # type: ignore[misc]
def get_player_stats(player_id : int) -> ResponseReturnValue:
    """Accesses a given player's stats"""
    cursor = get_db().cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT
                stat_type,
                stat_value,
                recorded_date
            FROM TrackedStatEntry
            WHERE player_id = %s AND is_visible = TRUE
            ORDER BY stat_value DESC, recorded_date DESC
        """, (player_id,))
        return jsonify(cursor.fetchall()), 200
    except Error as e:
        current_app.logger.error(f"Error in get_player_stats: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


@casual.route("/players/<int:player_id>/notifications", methods=["GET"]) # type: ignore[misc]
def get_player_notifications(player_id : int) -> ResponseReturnValue:
    """Accesses a given player's notifications"""
    cursor = get_db().cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT
                n.notification_id,
                g.event_name,
                g.event_type,
                g.start_date,
                g.end_date,
                g.description,
                n.read_status
            FROM Notification n
            JOIN GameEvent g ON n.event_id = g.event_id
            WHERE n.player_id = %s
            ORDER BY g.start_date ASC
        """, (player_id,))
        return jsonify(cursor.fetchall()), 200
    except Error as e:
        current_app.logger.error(f"Error in get_player_notifications: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


@casual.route("/players/<int:player_id>/goals", methods=["GET"]) # type: ignore[misc]
def get_player_goals(player_id : int) -> ResponseReturnValue:
    """Accesses a given player's goals"""
    cursor = get_db().cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT *
            FROM Goal
            WHERE player_id = %s
            ORDER BY start_date DESC
        """, (player_id,))
        return jsonify(cursor.fetchall()), 200
    except Error as e:
        current_app.logger.error(f"Error in get_player_goals: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()

@casual.route("/players/<int:player_id>/best-legends-weapons", methods=["GET"]) # type: ignore[misc]
def get_best_legends_weapons(player_id : int) -> ResponseReturnValue:
    """Accesses a given legend's best weapons"""
    cursor = get_db().cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT
                l.legend_name,
                plp.win_rate,
                plp.kd_ratio AS legend_kd,
                w.weapon_name,
                pwp.kd_ratio AS weapon_kd
            FROM PlayerLegendPerformance plp
            JOIN Legend l  ON plp.legend_id = l.legend_id
            JOIN PlayerWeaponPerformance pwp ON plp.player_id = pwp.player_id
            JOIN Weapon w  ON pwp.weapon_id  = w.weapon_id
            WHERE plp.player_id = %s
            ORDER BY plp.win_rate DESC, pwp.kd_ratio DESC
        """, (player_id,))
        return jsonify(cursor.fetchall()), 200
    except Error as e:
        current_app.logger.error(f"Error in get_best_legends_weapons: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


@casual.route("/players/<int:player_id>/goals", methods=["POST"]) # type: ignore[misc]
def add_goal(player_id : int) -> ResponseReturnValue:
    """Adds a goal"""
    cursor = get_db().cursor(dictionary=True)
    try:
        data = request.get_json()
        required = ["goal_type", "target_value", "start_date", "end_date"]
        for field in required:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        cursor.execute("""
            INSERT INTO Goal
                (player_id, goal_type, target_value, current_value,
                 start_date, end_date, goal_status)
            VALUES (%s, %s, %s, 0, %s, %s, 'In Progress')
        """, (player_id, data["goal_type"], data["target_value"],
              data["start_date"], data["end_date"]))
        get_db().commit()
        return jsonify({"message": "Goal created",
                        "goal_id": cursor.lastrowid}), 201
    except Error as e:
        current_app.logger.error(f"Error in add_goal: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


@casual.route("/players/stats/<int:stat_entry_id>/hide", methods=["PUT"]) # type: ignore[misc]
def hide_stat_entry(stat_entry_id: int) -> ResponseReturnValue:
    """Hides a player's stat entry"""
    cursor = get_db().cursor(dictionary=True)
    try:
        cursor.execute("""
            UPDATE TrackedStatEntry
            SET is_visible = FALSE
            WHERE stat_entry_id = %s
        """, (stat_entry_id,))
        get_db().commit()
        if cursor.rowcount == 0:
            return jsonify({"error": "Stat entry not found"}), 404
        return jsonify({"message": "Stat entry hidden"}), 200
    except Error as e:
        current_app.logger.error(f"Error in hide_stat_entry: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


@casual.route("/players/<int:player_id>/goals/<int:goal_id>", methods=["PUT"]) # type: ignore[misc]
def update_goal(player_id : int, goal_id : int) -> ResponseReturnValue:
    """Updates a player's goal"""
    cursor = get_db().cursor(dictionary=True)
    try:
        data = request.get_json()
        allowed = ["current_value", "goal_status", "end_date"]
        updates = [f"{f} = %s" for f in allowed if f in data]
        params  = [data[f] for f in allowed if f in data]

        if not updates:
            return jsonify({"error": "No valid fields to update"}), 400

        params += [player_id, goal_id]
        cursor.execute(
            f"UPDATE Goal SET {', '.join(updates)} WHERE player_id = %s AND goal_id = %s",
            params
        )
        get_db().commit()
        if cursor.rowcount == 0:
            return jsonify({"error": "Goal not found"}), 404
        return jsonify({"message": "Goal updated"}), 200
    except Error as e:
        current_app.logger.error(f"Error in update_goal: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


@casual.route("/players/<int:player_id>/goals/<int:goal_id>", methods=["DELETE"]) # type: ignore[misc]
def delete_goal(player_id : int, goal_id : int) -> ResponseReturnValue:
    """Deletes a player's goal"""
    cursor = get_db().cursor(dictionary=True)
    try:
        cursor.execute(
            "DELETE FROM Goal WHERE player_id = %s AND goal_id = %s",
            (player_id, goal_id)
        )
        get_db().commit()
        if cursor.rowcount == 0:
            return jsonify({"error": "Goal not found"}), 404
        return jsonify({"message": "Goal deleted"}), 200
    except Error as e:
        current_app.logger.error(f"Error in delete_goal: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
