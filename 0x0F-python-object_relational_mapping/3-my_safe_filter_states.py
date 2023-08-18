#!/usr/bin/python3
import MySQLdb as db
from sys import argv

"""
    a script that takes in an argument and displays
    all values in the states table of hbtn_0e_0_usa
    where name matches the argument.
"""
if __name__ == '__main__':
    db_conect = db.connect(host='localhost',
                           user=argv[1],
                           passwd=argv[2],
                           port=3306,
                           db=argv[3])

    db_cursor = db_conect.cursor()
    query = ("SELECT id, name FROM states WHERE name = %s \
            ORDER BY states.id ASC")

    name_to_match = argv[4]
    db_cursor.execute(query, (name_to_match,))

    selected_state = db_cursor.fetchall()
    for state in selected_state:
        print(state)
