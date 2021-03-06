### 24 / 06 / 2022
### Author: Michael Jonathan
### Creating my first class

class Book():
    """A class to create a book."""

    def __init__(self, name, price, publisher):
        """Intialize the name, price and publisher attributes"""

        self.name = name
        self.price = price
        self.publisher = publisher

    def hardback(self):
        """Slimulate a hardback book."""
        print(self.name.title() + " is a hardback book.")

    def softback(self):
        """Simulate a book being a softback book."""
        print(self.name.title() + "is a softback book.")

    def ebook(self):
        """Simulate an ebook"""
        print(self.name.title() + " is an ebook.")     

# Creating an instance of a book class.
my_book = Book('elon musk', 14.99, 'virgin books')     

my_book.hardback()