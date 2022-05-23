### 21 / 05 / 2022
### Author: Michael Jonathan
### Other ways to loop through a dictionary

birthday_months = {
    'michael' : 'may',
    'sarah' : 'april',
    'id' : 'march',
    'eniola' : 'febuary'
}

for name in birthday_months.keys():
    print(name.title())

for months in birthday_months.values():
    print(months.title())

for months in set (birthday_months.values()):
    print(months.title())        