from restaurant import Restaurant

my_restaurant = Restaurant('Yummy Yum', 'Dessert', 100)
my_restaurant.describe_restaurant()
my_restaurant.number_served = 100
my_restaurant.set_number(200)
my_restaurant.increment_number_served(150)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
#my_restaurant.display_flavors()