#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":

    arg = sys.argv[4]

    db = MySQLdb.connect(host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("""SELECT cities.name, states.name FROM states, cities WHERE states.name = %s""", (arg,))
    cities = cur.fetchall()

    for state in cities:
        print(state)

    cur.close()
    db.close()
