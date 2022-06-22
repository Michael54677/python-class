### 21 / 06 / 2022
### Author: Michael Jonathan
### Using arbitary keyword arguments

def seat_profile(first, last, **passenger_info):
    """Build a dictionary containing all passenger information"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in passenger_info.items():
        profile[key] = value
    return profile

passenger_profile = seat_profile('michael', 'jay', seat_number=67, breakfast = 'yes')

print(passenger_profile)
    