### 20 / 06 / 2022
### Author: Michael Jonathan
### using a while loop in a function


def get_formatted_name(first_name, last_name):
    """Return a full name neatly formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nWhat is your name?")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")

    formatted_name = get_formatted_name(first_name, last_name)

    print("\nHello Mr, " + formatted_name + "!")
