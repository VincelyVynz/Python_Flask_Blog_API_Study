from flask import Flask, request, jsonify
import sqlite3
app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Blog!'


if __name__ == '__main__':
    app.run(debug=True, port=5000)