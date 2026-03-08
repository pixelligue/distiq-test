def calculate_discount(price, discount_pct):
    # BUG: no validation, negative discount possible
    return price - (price * discount_pct / 100)

def find_user(db, user_id):
    # BUG: SQL injection risk
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return db.execute(query)
