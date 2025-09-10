from flask import Flask, request, jsonify
import sqlite3
app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Blog!'

@app.route('/posts')
def get_posts():

    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM posts')
    posts = cursor.fetchall()
    posts_list = []
    for row in posts:
        posts_list.append({'id': row[0], 'title': row[1], 'content': row[2], 'author': row[3], 'timestamp': row[4]})
    return jsonify(posts_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)