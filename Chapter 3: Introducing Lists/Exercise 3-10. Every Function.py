"""
Exercise 3-10. Every Function: Think of something you could store in a list. For example,
you could make a list of mountains, rivers, countries, cities, languages, or any-
thing else you’d like. Write a program that creates a list containing these items
and then uses each function introduced in this chapter at least once.
"""

countries = ["pakistan", "china", "japan", "korea", "thailand", "malaysia"]
print(countries)

# modifying list
countries[3] = "usa"
print(countries)

# using append
countries.append("uae")
print(countries)

# using insert
countries.insert(3, "korea")
print(countries)

# using pop method
countries.pop()
print(countries)

# using pop by index value
countries.pop(4)
print(countries)

# using remove method
countries.remove("korea")
print(countries)

# using del statement
del countries[3]
print(countries)

# using sort()
countries.sort()
print(countries)

# using sort reverse
countries.sort(reverse=True)
print(countries)

# using sorted
print(sorted(countries))

# using len
print(len(countries))

# using reverse
countries.reverse()
print(countries)
