from database.db import get_connection

def update_status(request_id, status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE service_requests SET status = ? WHERE request_id = ?",
        (status, request_id)
    )

    conn.commit()
    conn.close()
