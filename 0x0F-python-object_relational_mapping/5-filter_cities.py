#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_0_usa that belong to a given state."""
import MySQLdb
import sys

def get_cities_by_state(username, password, database, state_name):
    try:
        # Establish connection to the database
        db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database, port=3306)
        cursor = db.cursor()

        # Execute the SQL query with parameterization to avoid SQL injection
        query = """
            SELECT cities.name 
            FROM cities 
            INNER JOIN states ON states.id = cities.state_id 
            WHERE states.name = %s
        """
        cursor.execute(query, (state_name,))

        # Fetch all rows and extract city names
        city_names = [row[0] for row in cursor.fetchall()]

        # Print city names separated by commas
        print(", ".join(city_names))

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        # Close cursor and database connection
        if cursor:
            cursor.close()
        if db:
            db.close()

if __name__ == "__main__":
    # Check if correct number of command-line arguments are provided
    if len(sys.argv) != 5:
        print("Usage: python3 script_name.py <username> <password> <database> <state_name>")
        sys.exit(1)

    # Extract command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call function to get cities by state
    get_cities_by_state(username, password, database, state_name)

