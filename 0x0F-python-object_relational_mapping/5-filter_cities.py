#!/usr/bin/python3
<<<<<<< HEAD
"""  lists all states from the database hbtn_0e_0_usa """
"""
A script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows = cur.fetchall()
<<<<<<< HEAD
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
=======
    x = list(row[0] for row in rows)
    print(*x, sep=", ")
>>>>>>> 76a995ad7a3f61418ec390671e724d52e630da30
    cur.close()
    db.close()
