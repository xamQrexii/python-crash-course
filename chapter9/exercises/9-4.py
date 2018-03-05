class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant name is " +  self.restaurant_name.title() + " and cuisine type is " + self.cuisine_type.title())

    def open_restaurant(self):
        print("The restaurant is open now!")

    def set_number_served(self, number_served):
        self.number_served = number_served
        print(self.restaurant_name.title() + " has served " + str(self.number_served) + " customer(s)")

    def increment_number_served(self, number_served):
        self.number_served += number_served
        print(self.restaurant_name.title() + " has served " + str(self.number_served) + " customer(s)")

my_restaurant = Restaurant('kababjees', 'continental')
my_restaurant.set_number_served(20)
my_restaurant.increment_number_served(15)

