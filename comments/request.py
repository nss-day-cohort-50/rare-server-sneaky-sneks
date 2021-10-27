import sqlite3
import json
from sqlite3.dbapi2 import Date
from models import Post, User, Comment
from datetime import date

def get_comment_by_post(postId):
    
    with sqlite3.connect('./rare.db') as conn:
        
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT c.id,
        c.post_id,
        c.author_id,
        c.content,
        c.created_on
        FROM Comments c
        WHERE c.post_id = ?
        """, ( postId, ))

        dataset = db_cursor.fetchall()

        comments = []

        for row in dataset:
            comment = Comment(row['id'], row['post_id'], row['author_id'], row['content'], row['created_on'])

        comments.append(comment.__dict__)
    
    return json.dumps(comments)




