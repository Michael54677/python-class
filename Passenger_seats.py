### 21 / 06 / 2022
### Author: Michael Jonathan
### Using positional and arbitary arguments together.

def assign_seat(seat, *requests):
    """Assign a seat and requests to a passenger"""
    print("\nAssign seat number " + str(seat) + " the following passenger requests. ")
    for request in requests:
        print("- " + request) 

assign_seat(67, 'window seat')        