#!/usr/bin/python3
"""
script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa (SQL injection safe)
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def get_state_by_name():
    """Fetch and display the id of the State object matching the name"""
    arg = sys.argv
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(arg[1], arg[2], arg[3]),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Recherche sécurisée avec filter_by pour éviter SQL injection
    state = session.query(State).filter_by(name=arg[4]).first()
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    get_state_by_name()
