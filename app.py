from flask import Flask, render_template

app = Flask(__name__)

#Routes
from user import routes

#home page
@app.route('/')
def home():
    return render_template('home.html')


#dashboard page
@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')