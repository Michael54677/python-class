### 01 / 05 / 2022
### Author: Michael Jonathan
### Using a while loop to quite a program

prompt = "\nTo end this program enter 'q'."
prompt += "\nPlease enter your name: "
message = " "
while message != 'q':
    message = input(prompt)
    print(message)
