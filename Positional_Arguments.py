### 17 / 06 / 2022
### Author: Michael Jonathan
### Positional Arguments

# Creating our function
def book_description(book_type, author_name):
    """Displaying book information"""
    
    print("\nThis book is " + book_type + ".")
    print("The author of this book is " + author_name + ".")

book_description('non-fiction', 'ashlee vance')    
book_description('fiction', 'dan brown')