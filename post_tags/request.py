import sqlite3
import json
from models import Post_Tag, Tag


def get_all_post_tags():
    # Open a connection to the database
    with sqlite3.connect("./rare.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT pt.id pt_id,
        pt.post_id,
        pt.tag_id,
        t.id t_id,
        t.label
        FROM postTags pt
        LEFT JOIN Tags t on t_id = pt.tag_id
        """
        )

        dataset = db_cursor.fetchall()
        post_tags = []

        # Iterate list of data returned from database
        for row in dataset:
            post_tag = Post_Tag(row["pt_id"], row["post_id"], row['tag_id'])
            tag = Tag(row['t_id'], row['label'])
            post_tag.tag = tag.__dict__
            post_tags.append(post_tag.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(post_tags)


def create_post_tag(new_post_tag):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
        INSERT INTO PostTags
        (post_id, tag_id)
        VALUES (?,?)
        """,
            (new_post_tag["post_id"], new_post_tag["tag_id"]),
        )

        id = db_cursor.lastrowid
        new_post_tag["id"] = id

    return json.dumps(new_post_tag)

def get_tags_by_post_id(postId):
    with sqlite3.connect('./rare.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT 
            pt.id,
            pt.post_id,
            pt.tag_id
        FROM PostTags pt
        Where post_id = ?
        """, (postId,))

        tags=[]
        data = db_cursor.fetchall()
        for row in data:
            tag = Post_Tag(row['id'], row['post_id'], row['tag_id'])
            tags.append(tag.__dict__)
    return json.dumps(tags)

def update_tag(id, new_tag):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
        Update PostTags
        SET tag_id = ?
        WHERE id = ?
        """,
            (new_tag["tag_id"], id),
        )
        was_updated = db_cursor.rowcount

        if was_updated:
            return True
        else:
            return False
