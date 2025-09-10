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

@app.route('/posts', methods=['POST'])
def create_post():
    try:
        data = request.get_json()

        if 'title' not in data or not isinstance(data['title'], str) or data['title'].strip() == "":
            return jsonify({'error': 'Invalid or missing title'}), 400

        if 'content' not in data or not isinstance(data['content'], str) or data['content'].strip() == "":
            return jsonify({'error': 'Invalid or missing content'}), 400

        if 'author' not in data or not isinstance(data['author'], str) or data['author'].strip() == "":
            return jsonify({'error': 'Invalid or missing author'}), 400


        title = data['title']
        content = data['content']
        author = data['author']

        conn = sqlite3.connect('blog.db')
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO posts (title, content, author) VALUES (?, ?, ?)""", (title,content,author))
        conn.commit()

        post_id = cursor.lastrowid
        cursor.execute("SELECT * FROM posts WHERE id = ?", (post_id,))
        row = cursor.fetchone()

        post = {
            'id': row[0],
            'title': row[1],
            'content': row[2],
            'author': row[3],
            'timestamp': row[4]
        }
        conn.close()

        return jsonify(post), 201


    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)