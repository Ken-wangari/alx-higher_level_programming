#!/usr/bin/python3
""" Prints the State object with the name passed as argument from the database """

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database_name".format(sys.argv[0]))
        sys.exit(1)

    # Extract command-line arguments
    username, password, database_name = sys.argv[1:]

    try:
        # Create an engine to connect to the database
        engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}'
        )

        # Bind the engine to the Base class
        Base.metadata.bind = engine

        # Create a session maker
        Session = sessionmaker(bind=engine)

        # Create a session
        session = Session()

        # Query the database to retrieve the state name and corresponding city details
        query_result = session.query(State.name, City.id, City.name).join(City).all()

        # Print the query result
        for state_name, city_id, city_name in query_result:
            print(f"{state_name}: ({city_id}) {city_name}")

    except Exception as e:
        # Handle errors
        print("An error occurred:", e)
        sys.exit(1)

    finally:
        # Close the session
        session.close()

if __name__ == "__main__":
    main()

