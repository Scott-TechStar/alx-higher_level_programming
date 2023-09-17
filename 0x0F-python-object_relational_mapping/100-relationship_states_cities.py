#!/usr/bin/python3
"""adds the State object “California”
with the City “San Francisco”
to the database hbtn_0e_100_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

def create_state_city(username, password, db_name):
   engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)

    session.add(new_state)
    session.commit()

    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python 100-relationship_states_cities.py <username> <password> <db_name>")
    else:
        username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
        create_state_city(username, password, db_name)
