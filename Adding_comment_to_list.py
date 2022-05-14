### 05 / 05 / 2022
### Author: Michael Jonathan
### Adding comments to the Lists

# Creating a list of months
birthday_months = ['may', 'june', 'july',]
print(birthday_months)

#Changing an element of a List
birthday_months = ['Amy','june','july']
birthday_months[0] = 'May'
print(birthday_months)

#adding an element to a list using the append method
birthday_months.append('april')
print(birthday_months)

#Creating an empty list
birthday_months = []
print(birthday_months)

#Using the append method
birthday_months.append('october')
print(birthday_months)

#Using the insert method
birthday_months.insert(0, 'may')
print(birthday_months)

#Using the delete statment
del birthday_months[1]
print(birthday_months)