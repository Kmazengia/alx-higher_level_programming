#!/usr/bin/python3
"""
List all cities from a database
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    kefe = db.cursor()
    kefe.execute("SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = states.id;")
    states = kefe.fetchall()

    for state in states:
        print(state)
