#!/usr/bin/python3
"""Prints the State object with the name passed as an argument from the database."""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def print_state_and_cities(username, password, database, state_name):
    try:
        # Create engine and session
        engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query State object with the given name
        state = session.query(State).filter(State.name == state_name).first()

        if state:
            print(f"{state.id}: {state.name}")
            for city in state.cities:
                print(f"    {city.id}: {city.name}")
        else:
            print("State not found")

    except Exception as e:
        print("An error occurred:", e)

    finally:
        session.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 script_name.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]

    print_state_and_cities(username, password, database, state_name)

