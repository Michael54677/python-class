### 14 / 05 / 2022
### Author: Michael Jonathan
### Using the Or keyword to check values in a list

#Name registered
registered_name = ['michael', 'kola', 'id', 'ruth']

username = input("Please enter the user name you would like to use.")

#Check to see if usernmae is already taken
if username in registered_name:
    print("Sorry, username is already taken.")
else:
    print("This username is available.")
    
