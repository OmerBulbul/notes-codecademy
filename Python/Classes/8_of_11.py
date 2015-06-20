class Car(object):
    """Create a car object"""
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg

    def display_car(self):
        """Display car color, model and mpg using str() fucnction"""
        return "This is a " + self.color + " " + self.model + " with " + str(self.mpg) + " MPG."

    def display_car2(self):
        """Display car color, model and mpg using string formatting"""
        return "This is a %s %s with %s MPG." %( self.color, self.model, self.mpg)

    def drive_car(self):
        """Change the condition of a car"""
        self.condition = "used"

my_car = Car("DeLorean", "silver", 88)
print my_car.condition
my_car.drive_car()
print my_car.condition
