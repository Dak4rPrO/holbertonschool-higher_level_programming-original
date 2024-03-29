#!/usr/bin/python3
""" script that takes in the name of a state as an argument and lists
    all cities of that state, using the database hbtn_0e_4_usa """

import MySQLdb
import sys

if __name__ == "__main__":

    arg = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("""SELECT cities.name FROM states, cities
                WHERE cities.state_id = states.id
                AND states.name = %s""", (arg,))
    cities = cur.fetchall()

    try:
        for row in range(len(cities) - 1):
            print(cities[row][0], end=', ')
        print(cities[row + 1][0])
    except Exception:
        print()

    cur.close()
    db.close()
