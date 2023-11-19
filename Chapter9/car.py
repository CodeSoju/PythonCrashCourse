#Setting a Default value for an attribute
class Car:
    def __init__(self, make, model, year):
        """Initialize attribute to descirbe a car."""
        self.make = make
        self.model = model
        self.year =  year
        self.odometer_reading = 0
        self.gas_tank = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value
        Reject the change if it attempts to roll the odometer back. """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles
    
    def fill_gas_tank(self, gas_tank):
        """Fills up gas tank"""
        if self.gas_tank == 0:
            self.gas_tank = 100
        else:
            print(f"You have {self.gas_tank} gallons left.")

#Modifying Attribute Values
'''
a) change the value directly through an instance

b) set the value through a method

c)Increment the value through a method

'''

'''
Inheritance:
YOU don't always have to start from scratch when writing a class. If the class you
re writing is a specialized version of another class you wrote, you can use inheritance. 
When one class inherits from another, it takes on the attribute and methods of the first class. 
The original class is called the parent or all of the attributes and methods of its parent class, but's it's also free to 
define new attributes and methods of its own. 

The __init__() method for a Child Class:
=======================================
WHen you create a child class, the parent class must be part of the current file and must appear before the child
class in the file.
At the declaration of the ElectricCar class....
The name of the parent class must be included in the parentheses in the definition of a child class. 
The __init__() method inside the ElectricCar class takes in the information required to make a Car instance. 

The super() function at is a special function that allows you to call a method from the parent class . This line tells Pyton to call 
the __init__() method from Car, which gives an ElectricCar instance all the attributes defined in that method. The name
'super' comes from a convention of calling the parent class a 'superclass' and the child class a 'subclass'. 


You can override any method from the parent class that doesn't fit what you're trying to model w/ the child class. 
To do this, you define a method in the child class with the same name as the method you want to override. Python
will disregard the parent class method and only pay attention tp the method.

When you use inheritance, you can make your child classes retain what you need and override anything you don't from the parent class. 

INSTANCE AS ATTRIBUTES
-----------------------

'''