import httpx
import sqlite3 as sl

users_url = httpx.get('https://gorest.co.in/public/v2/users')
posts_url = httpx.get('https://gorest.co.in/public/v2/posts')
comments_url = httpx.get('https://gorest.co.in/public/v2/comments')
todos_url = httpx.get('https://gorest.co.in/public/v2/todos')

data_users = eval(users_url.text)
data_posts = eval(posts_url.text)
data_comments = eval(comments_url.text)
data_todos = eval(todos_url.text)

data_users = [tuple(el.values()) for el in data_users]
data_posts = [tuple(el.values()) for el in data_posts]
data_comments = [tuple(el.values()) for el in data_comments]
data_todos = [tuple(el.values()) for el in data_todos]

with sl.connect('socialnet.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    gender TEXT NOT NULL,
    status TEXT NOT NULL
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Posts (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    title TEXT NOT NULL,
    body TEXT NOT NULL
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Comments (
    id INTEGER PRIMARY KEY,
    post_id INTEGER,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    body TEXT NOT NULL
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Todos (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    title TEXT NOT NULL,
    due_on TEXT NOT NULL,
    status TEXT NOT NULL
    )''')

    cursor.executemany('INSERT INTO Users (id, name, email, gender, status) VALUES (?, ?, ?, ?, ?)', data_users)
    cursor.executemany('INSERT INTO Posts (id, user_id, title, body) VALUES (?, ?, ?, ?)', data_posts)
    cursor.executemany('INSERT INTO Comments (id, post_id, name, email, body) VALUES (?, ?, ?, ?, ?)', data_comments)
    cursor.executemany('INSERT INTO Todos (id, user_id, title, due_on, status) VALUES (?, ?, ?, ?, ?)', data_todos)