### 20 / 06 / 2022
### Author: Michael Jonathan
### Returning a dictionary

def build_book(name, author, publisher):
    """Create a dictionary of book information"""
    book = {'name' : name, 'author' : author, 'publisher' : publisher}
    return book

my_book = build_book('elon musk', 'ashlee vance', 'virgin book')
print(my_book)    