### 22 / 06 / 2022
### Author: Michael Jonathan
### Module / Importing an entire module


def books_available(*books):
    """Show a list of books available to buy."""
    for book in books:
        books_in_stock = "The following title is available to buy" + book.title() + "."
        print(books_in_stock)

  