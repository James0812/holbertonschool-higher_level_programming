#!/usr/bin/python3
"""
A module that contains a script that changes the name
of a State object from the database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def change_states():
    """
    Change the name of the State where id = 2 to New usa.
    """

    arg = sys.argv
    url_base = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    db_url = url_base.format(arg[1], arg[2], arg[3])
    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for inst in session.query(State).filter(State.name.like('%a%')):
        session.delete(inst)
    session.commit()


if __name__ == "__main__":
    change_states()
