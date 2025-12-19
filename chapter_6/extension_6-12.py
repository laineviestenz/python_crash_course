favorite_places = {
    'josh': ['beach', 'colorado'],
    'laine': ['NYC', 'Milwaukee'],
    'georgie': ['home']
}

for person, places in favorite_places.items():
    if len(places) > 1:
        print (person.title() + "'s favorite places are:")
        for place in places:
            print(place.title())
        print()
    else:
        print(person.title() + "'s favorite place is:")
        print(place)