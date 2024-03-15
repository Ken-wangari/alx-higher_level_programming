#!/usr/bin/python3
"""Start link class to table in database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Create a declarative base
Base = declarative_base()

# Define the State class
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database_name".format(sys.argv[0]))
        sys.exit(1)

    # Extract command-line arguments
    username, password, database_name = sys.argv[1:]

    try:
        # Create an engine to connect to the database
        engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost/{database_name}',
            pool_pre_ping=True
        )

        # Create the table if it doesn't exist
        Base.metadata.create_all(engine)

    except Exception as e:
        # Handle errors
        print("An error occurred:", e)
        sys.exit(1)

