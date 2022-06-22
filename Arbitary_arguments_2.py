### 21 / 06 / 2022
### Author: Michael Jonathan
### Arbitary_arguments 2

def create_passenger(*requests):
    """Passenger requests"""
    print("\nThis passenger has requested: ")
    for request in requests:
        print("- " + request)

create_passenger('Window seat', 'Top of plane','Breakfast')