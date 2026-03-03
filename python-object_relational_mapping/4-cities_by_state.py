#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
and displays each city with its state name.
"""

import MySQLdb
import sys


def list_cities():
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
    # Une seule requête SQL avec jointure pour récupérer ville + état
    cmd = ("SELECT cities.id, cities.name, states.name "
           "FROM cities "
           "JOIN states ON cities.state_id = states.id "
           "ORDER BY cities.id ASC")
    cursor.execute(cmd)
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    connection.close()


if __name__ == "__main__":
    list_cities()
