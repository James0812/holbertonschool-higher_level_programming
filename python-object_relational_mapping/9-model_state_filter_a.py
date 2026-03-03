#!/usr/bin/python3
"""
Module contains a  script that lists all State objects that
contain the letter a from the database hbtn_0e_6_usa.
"""


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def list_states():
    """
    Lists all State objects that
    contain the letter a from the database hbtn_0e_6_usa
    """

    arg = sys.argv
    url_base = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    db_url = url_base.format(arg[1], arg[2], arg[3])
    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for inst in session.query(State).filter(State.name.like('%a%')):
        print(inst.id, ": ", inst.name, sep="")


if __name__ == "__main__":
    list_states()
