def get_dashboard(user_id):
    return {
        "user": db.get_user(user_id),
        "orders": db.get_orders(user_id),
        "notifications": db.get_notifications(user_id)
    }