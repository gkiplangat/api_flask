from flask import Flask 

app=Flask(__name__)

#Home Page
@app.route('/')
@app.route('/home/')
def home():
    return "<h1>Home page</h1>"

# About Us Page
@app.route('/about/')
def about():
    return "<h1>About Us</h1>"

if __name__=='__main__':
    app.run(debug=True)
