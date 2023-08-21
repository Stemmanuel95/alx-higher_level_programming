#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ = "__main__":
    """This script connects to the mysql database
    and lists all the states from the database"""

    db_connection = MySQLdb.connect(
        host="localhost", user=sys.argv[1], passwd=sys.argv[2],
        db=sys.argv[3], port=3306)

    db_cursor = db_connection.cursor()

    db_cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    results_rows = db_cursor.fetchall()

    for results in results_rows:
        print(results)
