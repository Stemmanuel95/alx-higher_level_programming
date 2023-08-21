#!/usr/bin/python3
"""
listing all states with
name starting with `N`
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

"""
Connects to the database and extracts all states
from the database.
"""

if __name__ == '__main__':
    db_connection = MySQLdb.connect(host="localhost", port=3306,
                                    user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db_connection.cursor()

    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
