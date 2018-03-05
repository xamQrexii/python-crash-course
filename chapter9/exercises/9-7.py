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


# creating child class
class Admin(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ['can add post', 'can delete post', 'can ban user']






admin_1 = Admin('muhammad', 'osama')
admin_1.show_privileges()
