import os
import subprocess

AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
DB_PASSWORD = "super_secret_password_123"

def run_command(user_input):
    ""Execute user-provided command ? intentionally unsafe.""
    os.system(user_input)
    result = subprocess.call(user_input, shell=True)
    return result

def get_user(user_id):
    ""Fetch user with raw SQL ? intentionally unsafe.""
    import sqlite3
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.execute(f"SELECT * FROM users WHERE id = {user_id}")
    return cursor.fetchone()

def log_message(msg):
    ""Use print instead of structlog ? policy violation.""
    print(f"LOG: {msg}")

