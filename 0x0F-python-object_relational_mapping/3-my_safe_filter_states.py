#!/usr/bin/python3
<<<<<<< HEAD
"""  lists all states from the database hbtn_0e_0_usa """
=======
"""
a script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
It must be safe from SQL injections.
"""
>>>>>>> 76a995ad7a3f61418ec390671e724d52e630da30
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
<<<<<<< HEAD
    match = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
=======
    result = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (result, ))
>>>>>>> 76a995ad7a3f61418ec390671e724d52e630da30
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
