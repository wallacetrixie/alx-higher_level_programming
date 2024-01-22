#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        # Attempt to convert the value to an integer and print it
        integer_value = int(value)
        print("{:d}".format(integer_value))
        return True
    except ValueError as ve:
        # Print an error message to stderr if conversion fails
        print("Exception:", ve, file=sys.stderr)
        return False

# Example usage:
result = safe_print_integer_err(42)
print("Returned result:", result)

result = safe_print_integer_err("not_an_integer")
print("Returned result:", result)

