### 05 / 05 / 2022
### Author: Michael Jonathan
### Looping through a list

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

print(months[1])

#looping thorugh a list using a for loop
for month in months:
    print(month)

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
for month in months:
    print(month.title() + "is the name of a month")


months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']    
for month in months:
    print(month.title() + "\n")
    print("The next month is: ")

print("Goodbye")    