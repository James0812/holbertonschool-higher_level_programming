#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def fetch_states():
    """Fetch and display all State objects sorted by id"""
    arg = sys.argv
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(arg[1], arg[2], arg[3]),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Récupération de tous les états triés par id
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()


if __name__ == "__main__":
    fetch_states()
