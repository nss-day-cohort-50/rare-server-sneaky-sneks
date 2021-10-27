import sqlite3
import json
from sqlite3.dbapi2 import Date
from models import Post, User, Comment
from datetime import date

def get_all_posts():
    # Open a connection to the database
    with sqlite3.connect("./rare.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT *
        FROM Posts
        """)

        dataset = db_cursor.fetchall()
        posts = []

        # Iterate list of data returned from database
        for row in dataset:
            post = Post(row['id'],
                        row['user_id'],
                        row['category_id'],
                        row['title'],
                        row['publication_date'],
                        row['image_url'],
                        row['content'],
                        row['approved'])
            posts.append(post.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(posts)

def create_post(post):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        INSERT INTO posts
            (user_id, category_id, title, publication_date, image_url, content, approved)
        VALUES (?,?,?,?,?,?,?)
        """,
                (post['user_id'],
                post['category_id'],
                post['title'],
                post['publication_date'],
                post['image_url'],
                post['content'],
                post['approved']
                )
                )

        id = db_cursor.lastrowid
        post['id'] = id

    return json.dumps(post)

def get_posts_by_user(id):
    with sqlite3.connect('./rare.db') as conn:
            # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT p.id,
        p.user_id,
        p.category_id,
        p.title,
        p.publication_date,
        p.image_url,
        p.content,
        p.approved,
        u.id u_id,
        u.first_name,
        u.last_name
        FROM Posts p
        JOIN Users u ON u_id = p.user_id
        WHERE p.user_id = ?
        """, (id, ))

        dataset = db_cursor.fetchall()
        posts = []

        for row in dataset:
            post = Post(row['id'], row['user_id'], row['category_id'], row['title'],
                row['publication_date'], row['image_url'], row['content'], row['approved'])
            user = User(row['u_id'], row['first_name'], row['last_name'], '',
                '', '', '', '', '', '')

            post.user = user.__dict__
            posts.append(post.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(posts)

def get_post_by_id(postId):

    with sqlite3.connect('./rare.db') as conn:
        
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT p.id p_id,
        p.user_id,
        p.category_id,
        p.title,
        p.publication_date,
        p.image_url,
        p.content,
        p.approved,
        u.id u_id,
        u.first_name,
        u.last_name,
        c.id c_id,
        c.post_id c_postId,
        c.author_id,
        c.content c_content,
        c.created_on
        FROM Posts p
        JOIN Users u ON u_id = p.user_id
        JOIN Comments c ON c_postId = p.id
        WHERE p_id = ?
        """, ( postId, ))

        data = db_cursor.fetchone()

        comment_data = db_cursor.fetchall()
        comments = []

        post = Post(data['p_id'], data['user_id'], data['category_id'], data['title'],
                data['publication_date'], data['image_url'], data['content'], data['approved'])
        user = User(data['u_id'], data['first_name'], data['last_name'], '',
                '', '', '', '', '', '')
        
        for row in comment_data:
            comment = Comment(row['c_id'], row['c_postId'],
            row['author_id'], row['c_content'], row['created_on'])

            comments.append(comment.__dict__)

        post.comments = comments
        post.user = user.__dict__
        return json.dumps(post.__dict__)
