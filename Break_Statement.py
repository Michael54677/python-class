### 02 / 06 / 2022
### Author: Michael Jonathan
### Using break to exit a loop

prompt = "\nPlease enter the name of a book you have read recently?"
prompt += "\nTo end type 'q'."

while True:
    book = input(prompt)

    if book == 'q':
        break
    else:
        print("You have recently read" + book.title() + ".")
        
