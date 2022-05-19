### 14 / 05 / 2022
### Author: Michael Jonathan
### Using a key to get a value

# Creating a dictionary of terms
terms = {'variable' : 'represents or refers to a value stored in memory', 'string' : 'A sequence of characters.'}

if 'float' in terms:
    print("I know what a float is.")
else:
    print("I do not know what that is.")
print(terms['variable'])     

# Creating an empty dictionary
terms = {}

terms['variable'] = 'represents or refers to a value stored in memory'
terms['integer'] = 'A whole number.'

print(terms['variable'])
print(terms['integer'])


