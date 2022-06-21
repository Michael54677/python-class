### 20 / 06 / 2022
### Author: Michael Jonathan
### using a while loop in a function and break statement


def get_formatted_name(first_name, last_name):
    """Return a full name neatly formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nWhat is your name ? ")
    print("(press 'q' to end this program)")

    first_name = input("First Name: ")
    if first_name == 'q':
        break

    last_name = input("Last Name: ")
    if last_name == 'q':
        break

    formatted_name = get_formatted_name(first_name,last_name)
    print("\nHello Mr, " + formatted_name + "!")
