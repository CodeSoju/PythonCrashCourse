from car import Car

class Battery:
    """A simple attempy to model a battery for an electric car. """

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size. """
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """PRint a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge.")
    
    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles.
        Initialize attributes of the parent calss. 
        Then initialize attributes specfic to an electric car. 
    """

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}--kWh battery.")
    
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks"""
        print("This car doesn't have a gas tank!")

'''
The class ElectricCar needs access to its parent class Car, so we import Car directly
into the module at (1). IF we forget this line, Python will raise an error when we try
to import the electric_car module. We also need to update the Car module so it contains only the
Car class. 
'''