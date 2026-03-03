#!/usr/bin/python3
"""
script that prints the first State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def fetch_first_state():
    """Fetch and display the first State object by id"""
    arg = sys.argv
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(arg[1], arg[2], arg[3]),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Récupérer uniquement le premier objet State
    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    session.close()


if __name__ == "__main__":
    fetch_first_state()
