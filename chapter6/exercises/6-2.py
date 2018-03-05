favorite_numbers = {
    'anas': 5,
    'hamza': 18,
    'osama': 24,
    'ammar': 6,
    'ismail': 14
    }

# pring keys and values using loop

for k,v in favorite_numbers.items():
    if k[-1] == 's':
        print(k.title() + "' favorite number is " + str(v))
    else:
        print(k.title() + "'s favorite number is " + str(v))

