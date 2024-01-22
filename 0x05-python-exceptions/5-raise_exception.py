#!/usr/bin/python3
def raise_exception():
    try:
        # Raise a custom type exception
        raise ValueError("Custom type exception: This is a deliberate exception.")
    except ValueError as ve:
        # Catch the exception and print a message
        print("Caught an exception:", ve)
        # You can handle the exception further if needed
    finally:
        print("Finally block executed")

# Example usage:
raise_exception()

