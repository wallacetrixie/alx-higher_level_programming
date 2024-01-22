#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except Exception as e:
        print("Error:", e)
        return None
    else:
        print("Inside result: {}".format(result))
        return result
    finally:
        print("Finally block executed")

# Example usage:
result = safe_print_division(10, 2)
print("Returned result:", result)

result = safe_print_division(5, 0)
print("Returned result:", result)

