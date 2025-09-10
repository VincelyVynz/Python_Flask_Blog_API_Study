import sqlite3

conn = sqlite3.connect('blog.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS posts (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
content TEXT NOT NULL,
author TEXT NOT NULL,
timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)
''')
conn.commit()
conn.close()