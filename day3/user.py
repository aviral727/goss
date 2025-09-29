import hashlib

class User:
    users_db = {}  # simple dictionary as in-memory "database"

    def __init__(self, username, password):
        self.username = username
        self.password = self.hash_password(password)

    @staticmethod
    def hash_password(password):
        """Hash the password for security"""
        return hashlib.sha256(password.encode()).hexdigest()

    @classmethod
    def signup(cls, username, password):
        if username in cls.users_db:
            print("Username already exists.")
            return None
        user = User(username, password)
        cls.users_db[username] = user.password
        print(f"User {username} signed up successfully.")
        return user

    @classmethod
    def login(cls, username, password):
        hashed = cls.hash_password(password)
        if username not in cls.users_db:
            print("User not found.")
            return None
        if cls.users_db[username] != hashed:
            print("Incorrect password.")
            return None
        print(f"Welcome back, {username}!")
        return User(username, password)
