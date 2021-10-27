import sqlite3
import json
from models import Tag


def get_all_tags():
    # Open a connection to the database
    with sqlite3.connect("./rare.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT *
        FROM tags
        ORDER BY label asc
        """
        )

        dataset = db_cursor.fetchall()
        tags = []

        # Iterate list of data returned from database
        for row in dataset:
            tag = Tag(row["id"], row["label"])
            tags.append(tag.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(tags)


def create_tag(new_tag):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
        INSERT INTO Tags
        (label)
        VALUES (?)
        """,
            (new_tag["label"],),
        )

        id = db_cursor.lastrowid
        new_tag["id"] = id

    return json.dumps(new_tag)


def update_tag(id, new_tag):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
        Update Tags
        SET label = ?
        WHERE id = ?
        """,
            (new_tag["label"], id),
        )
        was_updated = db_cursor.rowcount

        if was_updated:
            return True
        else:
            return False


def delete_tag(id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
        DELETE FROM tags
        WHERE id = ?
        """,
            (id,),
        )
