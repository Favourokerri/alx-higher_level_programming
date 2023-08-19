#!/usr/bin/python3
"""
    a script that prints the first
    State object from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == '__main__':
    """
        script takes 3 arguments:
        mysql username,
        mysql password and database name
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    session = session()

    state = session.query(State).filter(State.id == 1).first()
    if state:
        print('{}: {}'.format(state.id, state.name))
    session.close()
