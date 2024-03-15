#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    # Establishing a connection to the database
    try:
        db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], port=3306)
        cursor = db.cursor()

        # Executing SQL query
        cursor.execute("SELECT * FROM states")

        # Fetching all rows
        rows = cursor.fetchall()

        # Printing each row
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("Error connecting to MySQL database:", e)

    finally:
        # Closing cursor and database connection
        if cursor:
            cursor.close()
        if db:
            db.close()

