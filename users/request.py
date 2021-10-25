import sqlite3
import json
from sqlite3.dbapi2 import Date
from models import User
from datetime import date

def get_all_users():
    # Open a connection to the database
    with sqlite3.connect("./rare.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT *
        FROM Users
        """)

        dataset = db_cursor.fetchall()
        users = []

        # Iterate list of data returned from database
        for row in dataset:
            user = User(row['id'],
                          row['first_name'],
                          row['last_name'],
                          row['email'],
                          row['bio'],
                          row['username'],
                          row['password'],
                          row['profile_image_url'],
                          row['created_on'],
                          row['active']
                          )
            users.append(user.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(users)

def create_user(user):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        INSERT INTO users
            (first_name, last_name, email, bio, username, password, profile_image_url, created_on, active)
        VALUES (?,?,?,?,?,?,?,?,?)
        """,
                          (user['first_name'],
                           user['last_name'],
                           user['email'],
                           "",
                           user['username'],
                           user['password'],
                           "", #profile_image_url
                           date.today(), #created_on
                           1
                           )
                          )

        id = db_cursor.lastrowid
        user['id'] = id
        user['token'] = user['id']

    return json.dumps(user)