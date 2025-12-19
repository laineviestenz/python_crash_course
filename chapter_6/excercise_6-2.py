favorite_numbers = {'jeff': 6, 'amy': 2, 'millie': 67, 'mandy': 4}

print()
for name in favorite_numbers:
    print(name.title() + "'s favorite number is " +
        str(favorite_numbers[name]) + "!")
print()

#change jeffs favorite number
favorite_numbers['jeff'] = 9
print()
for name in favorite_numbers:
    print(name.title() + "'s favorite number is " +
        str(favorite_numbers[name]) + "!")
print()