#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

def list_cities(username, password, db_name):
    engine = create_engine(f"mysql+mysqlconnector://{username}:{password}@localhost:3306/{db_name}")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print(f"{city.name} ({city.state.name})")

    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python list_cities.py <username> <password> <db_name>")
    else:
        username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
        list_cities(username, password, db_name)
