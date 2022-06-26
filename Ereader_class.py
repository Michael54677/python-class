### 25 / 06 / 2022
### Author: Michael Jonathan
### Creating a new ereader class

from email.errors import MalformedHeaderDefect


class Ereader():
    """A class to repesent an ereader."""

    def __init__(self, make, model, backlight, battery, screen_type):
        """inirialize the attributes of an ereader."""

        self.make = make
        self.model = model
        self.backlight = backlight
        self.battery = battery
        self.screen_type = screen_type

    def get_ereader_name(self):
        """Return a formatted descriptive name for the ereader."""
        long_name = self.make + ' - ' + self.model + ' - ' + self.backlight + ' - ' + self.battery + ' - ' + self.screen_type
        return long_name.title()

new_ereader = Ereader('Amazon Kindle', 'Paperwhite', 'Adjustable Backlight', 'Several Months of Battery Life', '300 Dpi') 
print(new_ereader.get_ereader_name())        