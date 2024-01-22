#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        # Raise a custom name exception with the provided message
        raise NameError(message)
    except NameError as ne:
        # Catch the exception and print the message
        print("Caught a NameError:", ne)
        # You can handle the exception further if needed
    finally:
        print("Finally block executed")

# Example usage:
raise_exception_msg("This is a custom message for the exception.")

