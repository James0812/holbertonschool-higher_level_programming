#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument safely.
"""

import MySQLdb
import sys


def search_safe():
    arg = sys.argv
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=arg[1],
        passwd=arg[2],
        db=arg[3],
        charset="utf8"
    )
    cursor = connection.cursor()
    # Requête sécurisée avec paramètres (%s)
    cmd = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(cmd, (arg[4],))
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    connection.close()


if __name__ == "__main__":
    search_safe()
