### 27 / 06 / 2022
### Author: Michael Jonathan
### Incrementing an attributes

class Ereader():
    """A class to repesent an ereader."""

    def __init__(self, make, model, backlight, battery, screen_type):
        """inirialize the attributes of an ereader."""

        self.make = make
        self.model = model
        self.backlight = backlight
        self.battery = battery
        self.screen_type = screen_type
        self.library_count = 0

    def get_ereader_name(self):
        """Return a formatted descriptive name for the ereader."""
        long_name = self.make + ' - ' + self.model + ' - ' + self.backlight + ' - ' + self.battery + ' - ' + self.screen_type
        return long_name.title()

    def read_library_count(self):
        """show the amount of ebooks in the kindle library."""
        print("You have " + str(self.library_count) + " books in your kindle libraby. ")    

    def update_library_count(self, ebook_count):
        """set the library count."""
        self.library_count = ebook_count

    def increment_library_count(self, purchased_ebooks):
        """Add the new ebooks to the library count."""
        self.library_count += purchased_ebooks   

class Kindlefire(Ereader):
    """Represents aspects of an ereader specific to a kindle Fire."""

    def __init__(self, make, model, backlight, battery, screen_type, screen_resloution='12'):
            """Initialize attributes for the Kindle fire
                Then intialize attribtues specific to a Kindle Fire."""

            super().__init__(make, model,backlight, battery, screen_type)

my_kindle_fire = Kindlefire('amazon', 'kindle fire', 'backlight', '12 hour battery life', 'color screen') 
print(my_kindle_fire.get_ereader_name())           