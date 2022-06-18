### 18 / 06 / 2022
### Author: Michael Jonathan
### Return value

def formatted_name(first_name,middle_name,last_name):
    """Returning a formatted name"""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

teacher = formatted_name('michael', 'ic', 'jonathan')
print(teacher)    

def get_formatted_username(email_address):
    """Return a formatted username"""
    username = email_address.strip()
    return username

user = get_formatted_username('michaeljonathan@example.com')
print(user)    