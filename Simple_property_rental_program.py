### 02 / 06 / 2022
### Author: Michael Jonathan
### Adding user input to a dictionary

# Create an empty dictionary
rental_properties = {}

# Set a flag to indicate we taking applications
rental_open = True

while rental_open:
    # prompt users for users name and address.
    username = input("\What is your name? ")
    rental_property = input("What is the address of the property that you have to rent? ")

    # Store the responses in a dictionary
    rental_properties[username] = rental_property

    # Ask if thr user knows anyone else looking to rent a property
    repeat = input("\nDo you know anyone who might like to rent out their property? ")
    if repeat == 'no':
        rental_open = False

    # Adding property is complete

print("\n--- Property to rent ---")
for username, rental_property in rental_properties.items():
    print(username + " has " + rental_property + " to rent. ")        
 