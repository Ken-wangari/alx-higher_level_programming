#!/usr/bin/python3

import sys

if __name__ == "__main__":
    """Print the addition of all arguments."""

    # Extract command-line arguments excluding the script name
    arguments = sys.argv[1:]

    # Check if there are arguments
    if not arguments:
        print("No arguments provided.")
    else:
        # Calculate the sum of arguments
        total = sum(int(arg) for arg in arguments)
        print("The sum is:", total)

