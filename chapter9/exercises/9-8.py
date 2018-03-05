class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = 0
        self.address = ''

    def describe_user(self, ):
        print("The user details as follows: \n"
              "User complete name: " + self.first_name + " " + self.last_name +
              "\nUser age is: " + str(self.age) +
              "\nUser address is: " + self.address)

    def greet_user(self):
        print("Hi " + self.first_name.title() + " " + self.last_name.title() + "! have a very good day to you!")


# creating privileges class

# creating admin class
class Admin(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


class Privileges():
    def __init__(self):
        self.privileges = ['chocolate']

    def show_privileges(self):
        print(self.first_name.title() + " " + self.last_name.title() + " has following rights:")
        for privilege in self.privileges:
            print(privilege.title())



