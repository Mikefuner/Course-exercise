import httpx
import sqlite3 as sl

def update_database():
    users_url = httpx.get('https://gorest.co.in/public/v2/users')
    posts_url = httpx.get('https://gorest.co.in/public/v2/posts')

    data_users = eval(users_url.text)
    data_posts = eval(posts_url.text)

    data_users = [tuple(el.values()) for el in data_users]
    data_posts = [tuple(el.values()) for el in data_posts]

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

        cursor.execute('DELETE FROM Users')
        cursor.execute('DELETE FROM Posts')
        cursor.executemany('INSERT INTO Users (id, name, email, gender, status) VALUES (?, ?, ?, ?, ?)', data_users)
        cursor.executemany('INSERT INTO Posts (id, user_id, title, body) VALUES (?, ?, ?, ?)', data_posts)
        conn.commit()