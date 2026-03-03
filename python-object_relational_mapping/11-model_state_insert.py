#!/usr/bin/python3
"""
script that adds the State object "Louisiana" to the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def insert_louisiana():
    """Add State 'Louisiana' and print its id"""
    arg = sys.argv
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(arg[1], arg[2], arg[3]),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Créer l'objet State
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Afficher l'id après insertion
    print(new_state.id)

    session.close()


if __name__ == "__main__":
    insert_louisiana()
