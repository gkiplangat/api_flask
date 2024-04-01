from flask import Flask, render_template, request, jsonify
from app import db  # Access the MongoClient instance from app.py
from user.models import User  # Import the User class

app = Flask(__name__)


# Signup route (handles POST requests)
@app.route('/signup', methods=['POST'])
def signup():
    try:
        # Print data for debugging (optional)
        print(f"Received form data: {request.form}")

        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        # Validate data (optional)

        # Create user object
        user = User(name=name, email=email, password=password)

        # Insert user into database
        user.signup(db)  # Call the signup method of the User class

        # Return success response
        return jsonify({'message': 'User created successfully!'}), 201

    except Exception as e:
        print(f"Error during signup: {e}")
        return jsonify({'error': 'Failed to create user'}), 500


if __name__ == '__main__':
    app.run()
