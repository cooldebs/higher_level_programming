#!/usr/bin/python3
<<<<<<< HEAD
"""  lists all states from the database hbtn_0e_0_usa """
=======
"""
a script that lists all cities from the database hbtn_0e_4_usa
"""
>>>>>>> 76a995ad7a3f61418ec390671e724d52e630da30
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
<<<<<<< HEAD
    cur.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
=======
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
                INNER JOIN states ON states.id=cities.state_id""")
>>>>>>> 76a995ad7a3f61418ec390671e724d52e630da30
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
