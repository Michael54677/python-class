### 05 / 05 / 2022
### Author: Michael Jonathan
### Creating a list of numbers

#Convert numbers into a list
numbers = list(range(1,7))
print(numbers)

odd_numbers = list(range(1,101, 2))
print(odd_numbers)

squares = []
for value in range(1,20):
    square = value ** 2
    squares.append(square)
    print(squares)

digits = [1,2,3,4,5,6,7,8,9,10]
print(min(digits)) 
print(max(digits)) 
print(sum(digits))  