#!/usr/bin/python3
"""
script that deletes all State objects with a name containing 'a'
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_a():
    """Delete all State objects whose name contains 'a'"""
    arg = sys.argv
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(arg[1], arg[2], arg[3]),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Récupérer tous les états contenant 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()

    session.close()


if __name__ == "__main__":
    delete_states_a()
