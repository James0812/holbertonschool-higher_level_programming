#!/usr/bin/python3
"""
script that prints all City objects from the database
hbtn_0e_14_usa sorted by cities.id
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def fetch_cities_by_state():
    """Fetch and print all cities with their state"""
    arg = sys.argv
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(arg[1], arg[2], arg[3]),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Join City and State to print <state name>: (<city id>) <city name>
    results = session.query(City, State).join(State, City.state_id == State.id).order_by(City.id).all()
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()


if __name__ == "__main__":
    fetch_cities_by_state()
