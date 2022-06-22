### 21 / 06 / 2022
### Author: Michael Jonathan
### Modifying a list in a function

def passengers(not_checked_in, checked_in):
    """Simulate passengers who are not checked in."""

    while not_checked_in:
        current_passenger = not_checked_in.pop()

        # Simulate checking a passenger in.
        print("Checking in passenger: " + current_passenger)
        checked_in.append(current_passenger)

def show_checked_in_passengers(checked_in):
    """Show all the passengers who have checked in."""
    print("\nThe following passengers have been checked in: ")
    for passengers in checked_in:
        print(passengers)

not_checked_in = ["Michael Jay", "Mary Murphy", "Sam smith"]
checked_in = []

passengers(not_checked_in, checked_in)
show_checked_in_passengers(checked_in)
