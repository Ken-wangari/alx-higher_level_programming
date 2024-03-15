#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco" from a DB
"""
import sys
from relationship_state import Base, State
from relationship_city import City
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
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}',
            pool_pre_ping=True
        )

        # Bind the engine to the Base class
        Base.metadata.bind = engine

        # Create a session maker
        Session = sessionmaker(bind=engine)

        # Create a session
        session = Session()

        # Create a new State object for California
        california = State(name='California')

        # Create a new City object for San Francisco
        san_francisco = City(name='San Francisco')

        # Append San Francisco to California's list of cities
        california.cities.append(san_francisco)

        # Add both objects to the session
        session.add(california)
        session.add(san_francisco)

        # Commit the transaction
        session.commit()

        print("Successfully added California with San Francisco to the database.")

    except Exception as e:
        # Handle errors
        print("An error occurred:", e)
        sys.exit(1)

    finally:
        # Close the session
        session.close()

if __name__ == '__main__':
    main()

