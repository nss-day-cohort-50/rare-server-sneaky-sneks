import sqlite3
import json
from sqlite3.dbapi2 import Date
from models import Post, User, Category
from datetime import date


def get_all_posts():
    # Open a connection to the database
    with sqlite3.connect("./rare.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT
        p.id,
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
        c.id cat_id,
        c.label
        FROM Posts p
        JOIN users u on p.user_id = u_id
        left JOIN categories c on p.category_id = c.id
        ORDER BY publication_date desc
        """
        )

        dataset = db_cursor.fetchall()
        posts = []

        # Iterate list of data returned from database
        for row in dataset:
            post = Post(
                row["id"],
                row["user_id"],
                row["category_id"],
                row["title"],
                row["publication_date"],
                row["image_url"],
                row["content"],
                row["approved"],
            )
            user = User(
                row["id"],
                row["first_name"],
                row["last_name"],
                "",
                "",
                "",
                "",
                "",
                "",
                "",
            )
            category = Category(row["id"], row["label"])
            post.user = user.__dict__
            post.category = category.__dict__
            posts.append(post.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(posts)


def create_post(post):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
        INSERT INTO posts
            (user_id, category_id, title, publication_date, image_url, content, approved)
        VALUES (?,?,?,?,?,?,?)
        """,
            (
                post["user_id"],
                post["category_id"],
                post["title"],
                post["publication_date"],
                post["image_url"],
                post["content"],
                post["approved"],
            ),
        )

        id = db_cursor.lastrowid
        post["id"] = id

        for tag in post['tagIds']:
            db_cursor.execute("""
            INSERT INTO PostTags
                (post_id, tag_id)
                VALUES (?, ?)
            """, (id, tag))

            

    return json.dumps(post)


def get_posts_by_user(id):
    with sqlite3.connect("./rare.db") as conn:
        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT
        p.id,
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
        c.id cat_id,
        c.label
        FROM Posts p
        JOIN users u on p.user_id = u_id
        left JOIN categories c on p.category_id = c.id
        WHERE p.user_id = ?
        ORDER BY publication_date desc
        """,
            (id,),
        )

        dataset = db_cursor.fetchall()
        posts = []

        for row in dataset:
            post = Post(
                row["id"],
                row["user_id"],
                row["category_id"],
                row["title"],
                row["publication_date"],
                row["image_url"],
                row["content"],
                row["approved"],
            )
            user = User(
                row["u_id"],
                row["first_name"],
                row["last_name"],
                "",
                "",
                "",
                "",
                "",
                "",
                "",
            )
            category = Category(row["id"], row["label"])

            post.user = user.__dict__
            post.category = category.__dict__
            posts.append(post.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(posts)


def get_post_by_id(postId):

    with sqlite3.connect("./rare.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
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
        FROM Posts p
        JOIN Users u on u_id = p.user_id
        WHERE p_id = ?
        """,
            (postId,),
        )

        data = db_cursor.fetchone()

        post = Post(
            data["p_id"],
            data["user_id"],
            data["category_id"],
            data["title"],
            data["publication_date"],
            data["image_url"],
            data["content"],
            data["approved"],
        )
        user = User(
            data["u_id"],
            data["first_name"],
            data["last_name"],
            "",
            "",
            "",
            "",
            "",
            "",
            "",
        )

        post.user = user.__dict__
        return json.dumps(post.__dict__)


def delete_post(id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
        DELETE FROM posts
        WHERE id = ?
        """,
            (id,),
        )


def update_post(new_post, id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
        Update posts
        Set user_id = ?,
        category_id = ?,
        title = ?,
        publication_date = ?,
        image_url = ?,
        content = ?,
        approved = ?
        WHERE id = ?
        """,
            (
                new_post["user_id"],
                new_post["category_id"],
                new_post["title"],
                new_post["publication_date"],
                new_post["image_url"],
                new_post["content"],
                new_post["approved"],
                id,
            ),
        )
        was_updated = db_cursor.rowcount

        if was_updated:
            return True
        else:
            return False
