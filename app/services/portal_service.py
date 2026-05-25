def get_dashboard(user_id):
    return {
        "user": db.get_user(user_id),
        "orders": db.get_orders(user_id),
        "notifications": db.get_notifications(user_id)
    }

def fetch_recent_orders(user_id):
    return db.query(
        "SELECT * FROM orders WHERE user_id=%s LIMIT 5",
        user_id
    )

def fetch_notifications(user_id):
    return db.query(
        "SELECT * FROM notifications WHERE user_id=%s",
        user_id
    )

def validate_orders(data):
    return data if data else []

def fetch_support_tickets(user_id):
    return db.query(
        "SELECT * FROM support_tickets WHERE user_id=%s",
        user_id
    )