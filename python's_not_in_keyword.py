### 14 / 05 / 2022
### Author: Michael Jonathan
### Checking if a value is not in a list

# Admin users
admin_users = ['michael', 'Eniola']

# Ask for username
usernmae = input("Please enter your username : ")

# Check if user is an admin user
if usernmae not in admin_users:
    print("You do not have access.")
else:
    print("Access granted.")
