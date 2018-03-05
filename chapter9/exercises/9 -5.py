class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = 0
        self.address = ''
        self.login_attempts = 0

    def describe_user(self,):
        print("The user details as follows: \n"
              "User complete name: " + self.first_name + " "+ self.last_name +
              "\nUser age is: " + str(self.age) +
              "\nUser address is: " + self.address)

    def greet_user(self):
        print("Hi " + self.first_name.title() + " " + self.last_name.title() + "! have a very good day to you!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print("The number of login attempts: " + str(self.login_attempts))

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("The number of login attempts: " + str(self.login_attempts))

user_one = User('muhammad', 'osama')
user_one.increment_login_attempts()
user_one.increment_login_attempts()
user_one.increment_login_attempts()
user_one.increment_login_attempts()
user_one.reset_login_attempts()
user_one.increment_login_attempts()

