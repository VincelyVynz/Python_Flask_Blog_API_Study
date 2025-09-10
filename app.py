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


@app.route('/posts/<int:id>')
def get_post(id):
    try:
        conn = sqlite3.connect('blog.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM posts WHERE id = ?""", (id,))
        row = cursor.fetchone()
        if row is None:
            return jsonify({'error': 'No such post'}), 404
        post = {'id': row[0], 'title': row[1], 'content': row[2], 'author': row[3], 'timestamp': row[4]}
        conn.close()
        return jsonify(post), 200
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500


@app.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):

    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid request'}), 400
    try:
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
        cursor.execute("SELECT * FROM posts WHERE id = ?", (id,))
        row = cursor.fetchone()
        if row is None:
            return jsonify({'error': 'No such post'}), 404
        cursor.execute("UPDATE posts SET title = ?, content = ?, author = ? WHERE id = ?",(title, content, author, id))
        conn.commit()
        cursor.execute("SELECT * FROM posts WHERE id = ?", (id,))
        updated_row = cursor.fetchone()
        id = updated_row[0]
        title = updated_row[1]
        content = updated_row[2]
        author = updated_row[3]
        timestamp = updated_row[4]
        conn.close()
        return jsonify({'id': id, 'title': title, 'content': content, 'author': author, 'timestamp': timestamp}), 200

    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    conn = None
    try:
        conn = sqlite3.connect('blog.db')
        cursor = conn.cursor()
        cursor.execute("""DELETE FROM posts WHERE id = ?""", (id,))
        if cursor.rowcount == 0:
            return jsonify({'error': 'No such post'}), 404
        else:
            conn.commit()
            return jsonify({'message': "Post deleted successfully."}), 200

    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500

    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    app.run(debug=True, port=5000)