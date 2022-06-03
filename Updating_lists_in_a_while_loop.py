### 02 / 06 / 2022
### Author: Michael Jonathan
### working with while loops and list

# Create a list of unconfirmed users
unconfirmed_users = ['michael', 'eniola', 'ruth', 'id']

# Add an empty list to hold confirmed users
confirmed_users = []

# Verify each user untill there are no more unconfirmed users.
# Move each confirmed user into the list of confirmed users.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# Displaying all confirmed users
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())    
