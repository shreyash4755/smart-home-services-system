from database.db import get_connection

def assign_technician(request_id, tech_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE service_requests SET assigned_tech = ?, status = ? WHERE request_id = ?",
        (tech_id, "In Progress", request_id)
    )

    conn.commit()
    conn.close()
