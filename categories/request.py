import sqlite3
import json
from models import Category


def get_all_categories():
    # Open a connection to the database
    with sqlite3.connect("./rare.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute(
            """
        SELECT *
        FROM categories
        ORDER BY label asc
        """
        )

        dataset = db_cursor.fetchall()
        categories = []

        # Iterate list of data returned from database
        for row in dataset:
            category = Category(row["id"], row["label"])
            categories.append(category.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(categories)


def create_category(new_cat):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
        INSERT INTO Categories
        (label)
        VALUES (?)
        """,
            (new_cat["label"],),
        )

        id = db_cursor.lastrowid
        new_cat["id"] = id

    return json.dumps(new_cat)


def update_category(id, new_cat):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
        Update Categories
        SET label = ?
        WHERE id = ?
        """,
            (new_cat["label"], id),
        )
        was_updated = db_cursor.rowcount

        if was_updated:
            return True
        else:
            return False


def delete_category(id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(
            """
        DELETE FROM categories
        WHERE id = ?
        """,
            (id,),
        )
