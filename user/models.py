from flask import Flask, jsonify
from passlib.hash import pbkdf2_sha256
import uuid


class User:

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def signup(self, db):
        # Print data for debugging (optional)
        print(f"User data: {self.__dict__}")

        # Encrypt the password
        self.password = pbkdf2_sha256.encrypt(self.password)

        # Create user object
        user_data = {
            "_id": uuid.uuid4().hex,
            "name": self.name,
            "email": self.email,
            "password": self.password,
        }

        # Insert user into database
        db.users.insert_one(user_data)


if __name__ == '__main__':
    app = Flask(__name__)
    # ... (optional code if running the model directly)
