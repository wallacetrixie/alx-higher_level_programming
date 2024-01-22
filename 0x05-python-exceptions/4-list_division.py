#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for i in range(list_length):
            try:
                # Try to divide corresponding elements of my_list_1 and my_list_2
                result = my_list_1[i] / my_list_2[i]
                result_list.append(result)
            except ZeroDivisionError:
                # Handle division by zero
                print("division by 0")
                result_list.append(0)
            except (TypeError, ValueError):
                # Handle cases where elements are not numbers
                print("wrong type")
                result_list.append(0)
            except IndexError:
                # Handle out of range case
                print("out of range")
                result_list.append(0)
    finally:
        return result_list

