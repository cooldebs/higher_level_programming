#!/usr/bin/python3
"""
a script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
It must be safe from SQL injections.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    result = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (result, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
