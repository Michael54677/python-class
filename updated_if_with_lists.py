### 14 / 05 / 2022
### Author: Michael Jonathan
### Using IF statements with lists

# Creating our shopping cart
shopping_cart = ['pens', 'paper', 'stapler', 'post-its']

# Adding each item to an order.
for item in shopping_cart:
    if item == 'stapler':
        print("Sorry this item is out of stock.")
    else:
        print("Adding" + item + "to your order.")
print("Your order is complete.")        
