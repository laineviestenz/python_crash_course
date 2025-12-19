favorite_places = {
    'josh': ['beach', 'colorado'],
    'laine': ['NYC', 'Milwaukee'],
    'georgie': ['home']
}

for person, places in favorite_places.items():
    print (person.title() + "'s favorite places are:")
    for place in places:
        print(place.title())
    print()