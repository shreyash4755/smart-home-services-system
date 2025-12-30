from database.db import get_connection
from services.genai_service import classify_issue

def create_service_request(user_id, issue):
    category, priority = classify_issue(issue)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """INSERT INTO service_requests 
           (user_id, issue, status, category, priority)
           VALUES (?, ?, ?, ?, ?)""",
        (user_id, issue, "Open", category, priority)
    )

    conn.commit()
    conn.close()

    return category, priority
