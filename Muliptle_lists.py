### 14 / 05 / 2022
### Author: Michael Jonathan
### Working with multiple lists

in_stock = ['blue pens', 'paper', 'staples']

shopping_cart = ['blue pens', 'paper', 'staples', 'orange post-its']

for item in shopping_cart:
    if item in in_stock:
        print("Adding " + item + " to your order.")
    else:
        print("Sorry " + item + " is not im stock.")
print("Your order is complete.")        