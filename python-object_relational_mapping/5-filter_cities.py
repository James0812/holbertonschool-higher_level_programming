#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state in the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def filter_cities():
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
    # Requête sécurisée avec paramètre pour éviter SQL injection
    cmd = ("SELECT cities.name FROM cities "
           "JOIN states ON cities.state_id = states.id "
           "WHERE states.name = %s "
           "ORDER BY cities.id ASC")
    cursor.execute(cmd, (arg[4],))
    results = cursor.fetchall()
    # Affichage séparé par des virgules
    cities_list = [row[0] for row in results]
    print(", ".join(cities_list))
    cursor.close()
    connection.close()


if __name__ == "__main__":
    filter_cities()
