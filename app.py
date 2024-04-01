from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Database connection details (consider placing this in a separate config file)
client = MongoClient("mongodb://localhost:27017/")
db = client["login_api_flask"]

# Routes (import from user.routes)
from user import routes

# Home page
@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
