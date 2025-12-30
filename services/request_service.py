from database.db import get_connection

def create_service_request(user_id, issue):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO service_requests (user_id, issue, status) VALUES (?, ?, ?)",
        (user_id, issue, "Open")
    )

    conn.commit()
    conn.close()
