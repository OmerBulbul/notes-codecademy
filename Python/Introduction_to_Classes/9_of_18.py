class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self):  # Remember to add `self` as an argument of a method!
        print self.name
        print self.age

hippo = Animal("Hipopon", 3)
hippo.description()

sloth = Animal("Namaken", 2)
ocelot = Animal("William", 3)

print hippo.health  
print sloth.health
print ocelot.health
