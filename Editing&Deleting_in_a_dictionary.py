### 21 / 05 / 2022
### Author: Michael Jonathan
### Editing & Deleting values is a dictionary

terms = {'integer' : 'is a number that contains a decimal point.'}

# Editing a key value
terms['integer'] = 'A whole number'

print(terms.get('integer'))

# Deleting a key value

terms = {'integer' : 'is a number that contains a decimal point.', 'string' : 'a sequence of characters'}

del terms['integer']

print(terms)
