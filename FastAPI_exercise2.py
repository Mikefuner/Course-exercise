from fastapi import FastAPI
import sqlite3 as sl

app = FastAPI()

@app.get('/socialnet/users')
async def users_data():
    with sl.connect('socialnet.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Users')
        users = cursor.fetchall()

        for i in range(len(users)):
            users[i] = {'id': users[i][0], 'name': users[i][1], 'email': users[i][2], 'gender': users[i][3], 'status': users[i][4]}       
    return users[::-1]
    
@app.get('/socialnet/users/{user_id}')
async def user_id_data(user_id: int):
    with sl.connect('socialnet.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Users WHERE id = ?', (user_id,))
        user = cursor.fetchone()
    return {'id': user[0], 'name': user[1], 'email': user[2], 'gender': user[3], 'status': user[4]}

@app.get('/socialnet/posts/{user_id}')
async def user_posts_data(user_id: int):
    user_posts = []
    with sl.connect('socialnet.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Posts WHERE user_id = ?', (user_id,))
        posts = cursor.fetchall()

        for post in posts:
            user_posts.append({'id': post[0], 'user_id': post[1], 'title': post[2], 'body': post[3]})
    return user_posts[::-1]