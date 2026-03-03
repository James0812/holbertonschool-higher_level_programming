#!/usr/bin/python3
"""
Contains a script that prints all City objects from the database hbtn_0e_14_usa
"""


import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def print_cities():
    """
    Prints all City objects from the database hbtn_0e_14_usa.
    """

    arg = sys.argv
    url_base = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    db_url = url_base.format(arg[1], arg[2], arg[3])
    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    search = session.query(City, State).filter(City.state_id == State.id)
    for c, s in search:
        print(
            s.name,
            ': ',
            '(',
            c.id,
            ') ',
            c.name,
            sep=""
        )


if __name__ == "__main__":
    print_cities()
