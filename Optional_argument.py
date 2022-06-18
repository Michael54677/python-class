### 18 / 06 / 2022
### Author: Michael Jonathan
### Optional arguments

def formatted_name(first_name, last_name, middle_name):
    """Return a full name"""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

teacher = formatted_name('michael', 'ic', 'jonathan')
print(teacher) 


def formatted_name(first_name, last_name, middle_name):
    """Return a full name"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title() 

teacher = formatted_name('michael', 'jonathan', 'ic')
print(teacher)   

teacher = formatted_name('michael', 'jonathan')
print(teacher)
