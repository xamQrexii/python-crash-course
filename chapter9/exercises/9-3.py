class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = 0
        self.address = ''

    def describe_user(self,):
        print("The user details as follows: \n"
              "User complete name: " + self.first_name + " "+ self.last_name +
              "\nUser age is: " + str(self.age) +
              "\nUser address is: " + self.address)

    def greet_user(self):
        print("Hi " + self.first_name.title() + " " + self.last_name.title() + "! have a very good day to you!")

user_one = User("muhammad", 'osama')
user_one.describe_user()
user_one.greet_user()

user_two = User("anas", 'niazi')
user_two.describe_user()
user_two.greet_user()

