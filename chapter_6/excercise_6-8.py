clover = {
    "first_name": "clover", 
    "last_name": "Smith", 
    "age": "1",
    "type": "cat"
    }

spot = {
    "first_name": "Spot",
    "last_name": "Cooper",
    "age": "3",
    "type": "dog"
}

bubbles = {
    "first_name": "bubbles",
    "last_name": "Dawg",
    "age": "6 months",
    "type": "fish"
}

pets = [clover, spot, bubbles]

for pet in pets:
    print('First Name: ' + pet["first_name"].title())
    print('Last Name: ' + pet["last_name"].title())
    print('age: ' + pet["age"])
    print('type: ' + pet["type"].title() + "\n")