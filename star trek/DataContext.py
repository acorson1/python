import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_all_from_season(conn, season):
    cur = conn.cursor
    cur.execute("SELECT * FROM list WHERE season=?", (season,))

    rows = cur.fetchall()
    for row in rows:
        print(row)


def main():
    database = r"python/star trek/shows.db"

    conn = create_connection(database)
    with conn:
        print("query by season")
        select_all_from_season(conn, int(input("what season do you want a list of?")))

        print("query all")
        select_all(conn)
