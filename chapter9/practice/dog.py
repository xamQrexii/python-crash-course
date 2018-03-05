class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")


    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

my_dog = Dog('Willie', 6)
my_dog.roll_over()
my_dog.sit()

your_dog = Dog('lucy', 3)
your_dog.sit()
your_dog.roll_over()