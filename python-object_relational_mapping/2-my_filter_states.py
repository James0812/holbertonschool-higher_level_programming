#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""


import MySQLdb
import sys


def search():
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
    cmd = "SELECT * FROM states WHERE BINARY name=\
'{}' ORDER BY id ASC".format(arg[4])
    cursor.execute(cmd)
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    connection.close()


if __name__ == "__main__":
    search()
