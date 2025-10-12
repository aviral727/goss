from flask import Flask, render_template, request, redirect


app = Flask(__name__)

# Temporary in-memory database
posts = []

@app.route('/')
def home():
    username = "Aviral"
    return render_template('home.html', username=username, posts=posts)

@app.route('/add_post', methods=['POST'])
def add_post():
    content = request.form['content']
    posts.append(content)
    return redirect('/')

@app.route('/delete_post/<int:index>')
def delete_post(index):
    if 0 <= index < len(posts):
        posts.pop(index)
    return redirect('/')

@app.route('/clear_posts', methods=['POST'])
def clear_posts():
    global posts  # if posts is stored as a global variable
    posts = []  # clear all posts
    return redirect('/')  # go back to home page


if __name__ == '__main__':
    app.run(debug=True)
