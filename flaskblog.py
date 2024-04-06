from flask import Flask, render_template

app=Flask(__name__)

posts =[
    {
        'title':'Blog Post 1',
        'author': 'Gideon Kiplangat',
        'date_posted':'6 April 2024',
        'content': 'The is our first post, welcome'
    },
      {
        'title':'Blog Post 2',
        'author': 'Philip Kiprotich',
        'date_posted':'7 April 2024',
        'content': 'The is our second post, welcome'
    }
]

#Home Page
@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html', posts=posts)

# About Us Page
@app.route('/about/')
def about():
    return render_template('about.html')

if __name__=='__main__':
    app.run(debug=True)
