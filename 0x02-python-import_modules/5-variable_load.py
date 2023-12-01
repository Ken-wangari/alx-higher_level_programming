#!/usr/bin/python3

if __name__ == "__main__":
    """Print the value of variable a from variable_load_5."""

    try:
        from variable_load_5 import a
        print("The value of 'a' is:", a)
    except ImportError:
        print("Module 'variable_load_5' not found or 'a' is not defined.")

