### 10 / 05 / 2022
### Author: Michael Jonathan
### Or Condition

your_age = input("How old are you? ")
friends_age = input("How old is your friend? ")

if int(your_age) >= 18 or int(friends_age) >=18:
    print("Congrats, one of you is old enought to vote:")
else:
    print("Sorry one of you is too young to vote.")
    
