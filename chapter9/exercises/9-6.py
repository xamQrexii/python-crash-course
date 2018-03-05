class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant name is " +  self.restaurant_name.title() + " and cuisine type is " + self.cuisine_type.title())

    def open_restaurant(self):
        print("The restaurant is open now!")


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print(self.restaurant_name.title() + " has following ice cream flavors:")
        for flavor in self.flavors:
            print(flavor.title())

my_ice_cream_restaurant = IceCreamStand('alpine gelato', 'ice cream', ['pineapple', 'strawberry', 'chocolate'])
my_ice_cream_restaurant.display_flavors()
