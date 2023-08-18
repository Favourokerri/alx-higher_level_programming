#!/usr/bin/python3
import MySQLdb as db
from sys import argv

"""
    a script that lists all cities 
    from the database hbtn_0e_4_usa

"""
if __name__ =='__main__':
    """
        script takes 3 arguments:
        mysql username, mysql password
        and database name

    """
    db_connect = db.connect(host='localhost', user=argv[1], passwd=argv[2], port=3306, db=argv[3])
    db_cursor = db_connect.cursor

