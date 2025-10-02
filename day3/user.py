import hashlib
import sqlite3

class User:
    users_db = {}  # username -> User object

    def __init__(self, username, password):
        self.username = username
        self.password = self.hash_password(password)
        self.status = "offline"
        self._create_table()

    @staticmethod
    def hash_password(password):
        """Hash the password for security"""
        return hashlib.sha256(password.encode()).hexdigest()

    def _create_table(self):
        conn = sqlite3.connect('social_media.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT,
                status TEXT
            )
        ''')

        conn.commit()
        conn.close()

    @classmethod
    def signup(cls, username, password):
        conn = sqlite3.connect("social_media.db")
        cursor = conn.cursor()
        try:
            hashed = cls.hash_password(password)
            cursor.execute("INSERT INTO users VALUES (?, ?, ?)", (username, hashed, "offline"))
            conn.commit()
            print(f"User {username} signed up successfully.")
        except sqlite3.IntegrityError:
            print("Username already exists.")
        conn.close()

    @classmethod
    def login(cls, username, password):
        conn = sqlite3.connect("social_media.db")
        cursor = conn.cursor()
        hashed = cls.hash_password(password)
        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        if not row:
            print("User not found.")
        elif row[0] != hashed:
            print("Incorrect password.")
        else:
            cursor.execute("UPDATE users SET status=? WHERE username=?", ("online", username))
            conn.commit()
            print(f"Welcome back, {username}!")
        conn.close()

    def logout(cls, username):
        conn = sqlite3.connect("social_media.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET status=? WHERE username=?", ("offline", username))
        conn.commit()
        conn.close()
        print(f"{username} logged out.")

    def get_all_users(cls):
        conn = sqlite3.connect("social_media.db")
        cursor = conn.cursor()
        cursor.execute("SELECT username, status FROM users")
        users = cursor.fetchall()
        conn.close()
        return users

    def delete_user(cls, username):
        conn = sqlite3.connect("social_media.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE username=?", (username,))
        conn.commit()
        conn.close()
        print(f"User {username} deleted.")
    
    def change_password(cls, username, old_password, new_password):
        conn = sqlite3.connect("social_media.db")
        cursor = conn.cursor()
        hashed_old = cls.hash_password(old_password)
        cursor.execute("SELECT password FROM users WHERE username=?", (username,))
        row = cursor.fetchone()
        if not row:
            print("User not found.")
        elif row[0] != hashed_old:
            print("Incorrect old password.")
        else:
            hashed_new = cls.hash_password(new_password)
            cursor.execute("UPDATE users SET password=? WHERE username=?", (hashed_new, username))
            conn.commit()
            print("Password changed successfully.")
        conn.close()

