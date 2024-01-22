#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as e:
        # Print an error message to stderr if an exception occurs
        print("Exception:", e, file=sys.stderr)
        return None

# Example usage:
def add_numbers(a, b):
    return a + b

def divide_numbers(a, b):
    return a / b

result1 = safe_function(add_numbers, 3, 4)
print("Result of add_numbers:", result1)

result2 = safe_function(divide_numbers, 8, 2)
print("Result of divide_numbers:", result2)

result3 = safe_function(divide_numbers, 5, 0)
print("Result of divide_numbers:", result3)

