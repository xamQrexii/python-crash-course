"""
Exercise 3-8. Seeing the World: Think of at least five places in the world you’d like to
visit.
•	 Store the locations in a list. Make sure the list is not in alphabetical order.
•	 Print your list in its original order. Don’t worry about printing the list neatly,
just print it as a raw Python list.
•	 Use sorted() to print your list in alphabetical order without modifying the
actual list.
•	 Show that your list is still in its original order by printing it.
•	 Use sorted() to print your list in reverse alphabetical order without chang-
ing the order of the original list.
•	 Show that your list is still in its original order by printing it again.
•	 Use reverse() to change the order of your list. Print the list to show that its
order has changed.
•	 Use reverse() to change the order of your list again. Print the list to show
it’s back to its original order.
•	 Use sort() to change your list so it’s stored in alphabetical order. Print the
list to show that its order has been changed.
•	 Use sort() to change your list so it’s stored in reverse alphabetical order.
Print the list to show that its order has changed.
"""

leisure_places = ["naran", "kaghan", "ansu lake", "china", "thailand"]
print(leisure_places) # printing list

print(sorted(leisure_places)) # printing list using sorted method (temporarily sorted)

print(leisure_places) # printing list again

# using reverse() to reverse the list
leisure_places.reverse()
print(leisure_places)

# using reverse() again to change the order of list (original order)
leisure_places.reverse()
print(leisure_places)

# using sort() to sort the list in alphabetical order permanently
leisure_places.sort()
print(leisure_places)

# using sort(reverse=True) to sort and reverse the list permanently
leisure_places.sort(reverse=True)
print(leisure_places)