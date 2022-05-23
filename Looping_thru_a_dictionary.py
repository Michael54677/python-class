### 21 / 05 / 2022
### Author: Michael Jonathan
### Looping through a dictionary

birthday_months = {
    'michael' : 'may',
    'sarah' : 'april',
    'id' : 'march',
    'eniola' : 'febuary'
}

print(birthday_months)

# Looping through key-value pairs
book_1 = {
    'name' : 'elon musk',
    'author' : 'ashlee vance',
    'price' : '14.99',
    'publisher' : 'virgin books',
}

for key, value in book_1.items():
    print("\nkey: " + key)
    print("value: " + value)


birthday_months = {
    'michael' : 'may',
    'sarah' : 'april',
    'id' : 'march',
    'eniola' : 'febuary'
}

for key, value in birthday_months.items():
    print("\nName: " + key)
    print("month: " + value)