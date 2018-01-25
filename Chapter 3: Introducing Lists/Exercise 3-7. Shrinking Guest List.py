"""
Exercise 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.
•	 Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
•	 Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.
•	 Print a message to each of the two people still on your list, letting them
know they’re still invited.
•	 Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program.
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

print("\n")

print("Guys, I am sorry to inform you that I can only invite two friends.")

print("\n")

# removing four friends from list using pop()
print(guests_list.pop().title() + ", I'm sorry, I can't invite you on dinner")
print(guests_list.pop().title() + ", I'm sorry, I can't invite you on dinner")
print(guests_list.pop().title() + ", I'm sorry, I can't invite you on dinner")
print(guests_list.pop().title() + ", I'm sorry, I can't invite you on dinner")

print("\n")

# inviting two friends who are still in list

print("Hi " + guests_list[0].title() + "! you are invited on dinner.")
print("Hi " + guests_list[1].title() + "! you are invited on dinner.")

# deleting elements from list using del()

del guests_list[0]
del guests_list[0]

print("\n")

# printing blank list

print("Blank list", guests_list)



