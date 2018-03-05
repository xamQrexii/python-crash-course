person = {
    'first_name': 'muhammad',
    'last_name': 'osama',
    'age': 28,
    'city': 'karachi'
}

# printing value of each key by defining one by one
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

print("**********")

# printing values of all key using for loop
for v in person.values():
    print(str(v).upper())
