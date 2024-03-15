#!/usr/bin/python3
"""Lists all cities and their corresponding states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

def list_cities_and_states(username, password, database):
    try:
        # Connect to the database
        db = MySQLdb.connect(host="localhost", user=username,
                             passwd=password, db=database, port=3306)
        
        # Create a cursor object
        cur = db.cursor()

        # Execute the SQL query to fetch cities and their corresponding states
        query = """
            SELECT cities.id, cities.name, states.name 
            FROM cities 
            INNER JOIN states 
            ON states.id = cities.state_id
        """
        cur.execute(query)

        # Fetch all rows from the result set
        rows = cur.fetchall()

        # Print the fetched rows
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        # Close cursor and database connection
        if cur:
            cur.close()
        if db:
            db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 script_name.py <username> <password> <database>")
        sys.exit(1)

    # Extract command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the function to list cities and states
    list_cities_and_states(username, password, database)

