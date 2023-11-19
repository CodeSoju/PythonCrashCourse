from car import Car
from electricCar import ElectricCar

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
#my_new_car.odometer_reading = 23
my_new_car.update_odometer(73)
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
#my_tesla.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

'''
As you add more functionality to your classes, your files can get long, even when you use inheritance properly. 
In keeping with the overall philosophy of Python, you'll want to keep your files as uncluttered as possible. 
To help, Python lets you store classes in modules and then import the classes you need into your main program. 

Importing a Single Class
------------------------
You should write a docstring for each module you create. 

The import statement st (1) tells Pyton to open the car module and import the class Car. 
Importing classes is an effective way to program. Picture how long this porgram
file would be if the entire Car class were included. When you instead move the class to a module
and import the module, you still get all the same functionality, but you keep your main program
file clean and easy to read. You also store most of the logic in separate files; once your classes
work as you want them to, you can leave those files alone and focus on the higher0-level logic of your main
program. 

IMporting an Entire Module
--------------------------
You cn also import an entire module and then access the classes you need using dot notation. 
eg: 

import car  (1)
my_beetle = car.Car('volkswagen', 'beetle', 2019)

At (1) we import the entire car module. We then acces the class we need through the module.ClassName 
syntax

IMPORTING ALL CLASSES FROM A MODULE
-----------------------------------
You cn an import every class from a module using the following syntax:

from module_name import *

This method is not recommended for two reasons. First, it's helpful to be able to read
the import statements at the top of a file and get a clear sense of
which classes a program uses. With this apporach it's unclear which classes
you're using from the module. This approach can lead to confusion with names in 
the file. If you accidentally import a class with the same name as something else in your program file, 
you can create errors that are hard to diagnose. 
If you need to import many classes from a module, you're better off importing the entire module
and using the module_name.ClassName syntax

IMPORTING A MODULE INTO A MODULE
---------------------------------
SOmetimes you'll want to spread out your classes over several modules to keep any one file
from growing too large and avoid storing unreleated classes in the same module. 
When you store your classes in several modules, you may find that a class in one module depends
on a class into the first module. 


USING ALIASES:
---------------
Aliases can be quite helpful when using modules to organize your projects' code. 
You can use aliases when importing classes as well. 

As an example, consider a program where you want to make a bunch of electric cars. It might get
tedious to type (and read) ElectricCar over and over again. You can give ElectricCar an alias in the 
import statement:

from electric_car import ElectricCar as EC

my_tesla = EC('tesla', 'roadster', 2019)
'''