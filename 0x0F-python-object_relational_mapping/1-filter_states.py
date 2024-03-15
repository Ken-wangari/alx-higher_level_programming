#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa whose names start with 'N'."""
import MySQLdb
import sys

def get_states_starting_with_N(username, password, database):
    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database, port=3306)
        cursor = db.cursor()

        # Execute the SQL query to select states starting with 'N'
        query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id"
        cursor.execute(query)

        # Fetch all rows and print them
        rows = cursor.fetchall()
        for row in rows:
            print(row)

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
    if len(sys.argv) != 4:
        print("Usage: python3 script_name.py <username> <password> <database>")
        sys.exit(1)

    # Extract command-line arguments
    username, password, database = sys.argv[1:]

    # Call function to get states starting with 'N'
    get_states_starting_with_N(username, password, database)

