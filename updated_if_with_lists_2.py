### 14 / 05 / 2022
### Author: Michael Jonathan
### Working with empty list

# Empty shopping cart
shopping_cart = []

if shopping_cart:
    for item in shopping_cart:
        print("Adding" + item + "to your cart.")
    print("Your order is complete.")
else:
    print("You must select an item before proceeding.")
