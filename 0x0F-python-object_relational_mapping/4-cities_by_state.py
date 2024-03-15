#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


def main():
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database_name".format(sys.argv[0]))
        sys.exit(1)

    # Extract command-line arguments
    username, password, database_name = sys.argv[1:]

    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database_name,
            port=3306
        )

        # Create a cursor object to execute SQL queries
        cur = db.cursor()

        # Execute the SQL query to fetch data from cities and states tables
        cur.execute("""
            SELECT cities.id, cities.name, states.name 
            FROM cities 
            INNER JOIN states 
            ON states.id = cities.state_id
        """)

        # Fetch all rows from the executed query
        rows = cur.fetchall()

        # Print fetched rows
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        # Handle MySQL errors
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        # Close cursor and database connection
        if cur:
            cur.close()
        if db:
            db.close()


if __name__ == "__main__":
    main()

