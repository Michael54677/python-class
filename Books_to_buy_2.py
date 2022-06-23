### 23 / 06 / 2022
### Author: Michael Jonathan
### How to import specific functions


def books_available(*books):
    """Show a list of books available to buy."""
    for book in books:
        books_in_stock = ("The following title is available to buy " + book.title() + ".")
        print(books_in_stock)

def book_description(author_name, book_type="non-fiction"):
    """Displaying book information"""

    print("This is a " + book_type + " book.")
    print("The author of this book is " + author_name.title() + ".")
        