#!/usr/bin/python3
"""
Displays all states in the database hbtn_0e_0_usa
where name matches the argument provided.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connexion à MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cur = db.cursor()
    # Requête avec format() strict
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
