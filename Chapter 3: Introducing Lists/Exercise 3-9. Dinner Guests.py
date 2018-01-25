"""
Exercise 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
through 3-7 (page 46), use len() to print a message indicating the number
of people you are inviting to dinner.
"""

guests_list = ['anas', 'ammar', 'ahsan']

print("Hi " + guests_list[0].title() + "! you are invited on dinner.")
print("Hi " + guests_list[1].title() + "! you are invited on dinner.")
print("Hi " + guests_list[2].title() + "! you are invited on dinner.")
print("I'm invinting total " + str(len(guests_list)) + " friends on dinner!")