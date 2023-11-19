class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name} and serve {self.cuisine_type} food. There are {self.number_served} customers. ")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
    
    def set_number(self, num_customers):
        self.number_served = num_customers
        return self.number_served
    
    def increment_number_served(self, add_customers):
        self.number_served += add_customers
        return self.number_served

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        super().__init__(restaurant_name, cuisine_type, number_served = 0)
        self.flavors = ["Vanilla, Strawberry, Chocolate, Rocky Road, Cookies'N Cream"]
    
    def display_flavors(self):
        for x in range(len(self.flavors)):
            print(self.flavors[x] + "\n")

    
'''
my_restaurant = IceCreamStand('Yummy Yum', 'Dessert', 100)
my_restaurant.describe_restaurant()
my_restaurant.number_served = 100
my_restaurant.set_number(200)
my_restaurant.increment_number_served(150)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.display_flavors()
'''
'''
person_one = User("Johnny", "Bravo", 5)
person_one.describe_user()
person_one.increment_login_attempts()
person_one.increment_login_attempts()
person_one.increment_login_attempts()
person_one.greet_user()
person_one.describe_user()
person_one.reset_login_attempts()
person_one.describe_user()

person_two = Admin("Adam", "Mink", 0)
person_two.privileges.show_privileges()
'''