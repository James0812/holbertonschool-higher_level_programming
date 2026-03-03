#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N) from the database
hbtn_0e_0_usa.
"""


import MySQLdb
import sys


if __name__ == "__main__":
    args = sys.argv
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=args[1],
        passwd=args[2],
        db=args[3],
        charset="utf8"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
ORDER BY id ASC")
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    connection.close()
