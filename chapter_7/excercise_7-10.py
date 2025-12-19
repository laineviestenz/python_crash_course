responses = {}
while True:
    name = input('what is your name? ')
    spot = input("what is your dream vacation? ")
    ask_again = input('ask another person? (y or n)')
    responses[name] = (spot)
    if ask_again == 'n':
        break

print(responses)
for name, spot in responses.items():
    print(name.title() + ' would like to visit ' + spot.title() + '.')
#empty comment