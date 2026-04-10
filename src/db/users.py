import sqlite3

def get_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # VULNERABLE: direct string concatenation
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)
    return cursor.fetchone()

def get_user_by_email(email):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # VULNERABLE: f-string in SQL
    query = f"SELECT * FROM users WHERE email = '{email}'"
    cursor.execute(query)
    return cursor.fetchone()

def delete_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # VULNERABLE: no parameterization
    cursor.execute("DELETE FROM users WHERE id = " + str(user_id))
    conn.commit()
