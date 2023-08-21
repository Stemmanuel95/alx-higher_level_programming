#!/usr/bin/python3

import MySQLdb as db
from sys import argv

"""
Script connects to the db and lists all states
from the database.
"""

if __name__ == "__main__":
    db_connection = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db_connection.cursor()

    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' \
                ORDER BY states.id ASC")

    results_rows = db_cursor.fetchall()

    for results in results_rows:
        print(row)
