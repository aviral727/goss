from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to My Social Media Backend!"

@app.route('/user')
def user():
    return "User profile endpoint"

@app.route('/posts')
def posts():
    return "List of all posts"

@app.route('/greet/<username>')
def greet(username):
    return f"Hello, {username}! Welcome to Social Media API"



if __name__ == '__main__':
    app.run(debug=True)
