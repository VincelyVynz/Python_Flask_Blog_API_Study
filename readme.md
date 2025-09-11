# 📝 Flask Blog API

This is a **learning project** built using **Flask** and **SQLite**. It provides a simple REST API to perform CRUD operations on blog posts. The project helped reinforce concepts like API design, request validation, status codes, and working with databases in Python.

⚠️ The `blog.db` SQLite database is **not included** in the repo. You can create it using the `init_db.py` script.

---

## 📦 Features

- 📄 **Create a Post** (`POST /posts`)
- 📥 **Retrieve All Posts** (`GET /posts`)
- 🔍 **Retrieve Single Post by ID** (`GET /posts/<id>`)
- 🛠️ **Update Entire Post** (`PUT /posts/<id>`)
- ✏️ **Partially Update a Post** (`PATCH /posts/<id>`)
- ❌ **Delete a Post** (`DELETE /posts/<id>`)

---

## 📁 File Overview

| File           | Description                                               |
|----------------|-----------------------------------------------------------|
| `app.py`       | Main Flask application and all API route logic            |
| `init_db.py`   | Script to initialize the SQLite database (`blog.db`)      |


---

## 🗃️ Database Setup

To create the SQLite database and `posts` table, run the following:

```bash
python init_db.py
```

This creates `blog.db` with a `posts` table:

```sql
CREATE TABLE IF NOT EXISTS posts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  content TEXT NOT NULL,
  author TEXT NOT NULL,
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🧪 API Endpoints Overview

| Method | Endpoint            | Description                          |
|--------|---------------------|--------------------------------------|
| GET    | `/`                 | Welcome message                      |
| GET    | `/posts`            | Fetch all blog posts                 |
| GET    | `/posts/<id>`       | Fetch a single post by ID            |
| POST   | `/posts`            | Create a new blog post               |
| PUT    | `/posts/<id>`       | Fully update an existing post        |
| PATCH  | `/posts/<id>`       | Partially update one or more fields  |
| DELETE | `/posts/<id>`       | Delete a post by ID                  |

---

## 🧾 JSON Format for Posts

For `POST`, `PUT`, and `PATCH` requests, send JSON like this:

```json
{
  "title": "My Blog Title",
  "content": "This is the blog content.",
  "author": "Author Name"
}
```

---

## 🚀 Run Locally

1. Install dependencies:
   ```bash
   pip install flask
   ```

2. Initialize the database:
   ```bash
   python init_db.py
   ```

3. Run the Flask app:
   ```bash
   python app.py
   ```

4. Open your browser or Postman:
   ```
   http://localhost:5000/posts
   ```

---

## 📌 Example cURL Commands

### ➕ Create a Post
```bash
curl -X POST http://localhost:5000/posts \
  -H "Content-Type: application/json" \
  -d '{"title":"Test","content":"Hello world","author":"Alice"}'
```

### 🛠️ Full Update
```bash
curl -X PUT http://localhost:5000/posts/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"Updated","content":"New content","author":"Bob"}'
```

### ✏️ Partial Update
```bash
curl -X PATCH http://localhost:5000/posts/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"Just Title Changed"}'
```

### ❌ Delete Post
```bash
curl -X DELETE http://localhost:5000/posts/1
```

---


## 📚 Why This Project?

I built this API as a **hands-on learning project** to better understand:

- Flask routing and request handling
- Working with SQLite in Python
- HTTP methods and status codes
- Handling JSON and validating input

---

## 📄 License

This project is for educational purposes and has no specific license. You're free to explore, modify, and use it however you like.
