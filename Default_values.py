### 17 / 06 / 2022
### Author: Michael Jonathan
### Default Values

# Creating a function
def book_description(author_name, book_type="non-fiction"):
    """Displaying book information"""

    print("\nThis is a " + book_type + " book.")
    print("The author of this book is " + author_name.title() + ".")

book_description('ashlee vance') 
   