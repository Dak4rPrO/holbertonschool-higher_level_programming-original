#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("""SELECT cities.id, cities.name, states.name FROM states, \
cities WHERE cities.state_id = states.id ORDER BY cities.id ASC""")
    cities = cur.fetchall()

    for state in cities:
        print(state)

    cur.close()
    db.close()
