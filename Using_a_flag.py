### 02 / 06 / 2022
### Author: Michael Jonathan
### Using a flag to stop a program

prompt = "\nEnter 'q' to end this program."
prompt += "\nWhat is your name? "

# Setting our flag to True
active = True
while active:
    message = input(prompt)

    if message == 'q':
        active = False
    else:
        print(message)
