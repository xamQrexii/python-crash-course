"""
Exercise 3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
•	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a
bigger dinner table.
•	 Use insert() to add one new guest to the beginning of your list.
•	 Use insert() to add one new guest to the middle of your list.
•	 Use append() to add one new guest to the end of your list.
•	 Print a new set of invitation messages, one for each person in your list.
"""

guests_list = ['anas', 'ammar', 'qasim']
print("Hey guys, I found bigger dinner table gonna invite three more friends\n")

# adding three more friends in guests_list
guests_list.insert(0, 'ismail')
guests_list.insert(2, 'ali')
guests_list.append('soban')

print("Hi " + guests_list[0].title() + "! you are invited on dinner.")
print("Hi " + guests_list[1].title() + "! you are invited on dinner.")
print("Hi " + guests_list[2].title() + "! you are invited on dinner.")
print("Hi " + guests_list[3].title() + "! you are invited on dinner.")
print("Hi " + guests_list[4].title() + "! you are invited on dinner.")
print("Hi " + guests_list[5].title() + "! you are invited on dinner.")