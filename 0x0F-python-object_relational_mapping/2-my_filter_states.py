#!/usr/bin/python3

"""
    a script that takes in an argument and displays
    all values in the states table of hbtn_0e_0_usa
    where name matches the argument.
"""
import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    """
        script takes 4 arguments:
        mysql username, mysql password,
        database name and state name searched
    """
    db_conect = db.connect(host='localhost',
                           user=argv[1],
                           passwd=argv[2],
                           port=3306,
                           db=argv[3])
    db_cursor = db_conect.cursor()
    db_cursor.execute("SELECT * FROM states")

    selected_state = db_cursor.fetchall()
    [print("{}".format(state))
     for state in selected_state if state[1] == argv[4]]
