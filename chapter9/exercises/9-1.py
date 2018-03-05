class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant name is " +  self.restaurant_name.title() + " and cuisine type is " + self.cuisine_type.title())

    def open_restaurant(self):
        print("The restaurant is open now!")

my_restaurant = Restaurant('kababjees', 'continental')
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()