import json
"""check if a favorite number is already stored, and if not request favorite number and store it"""

filename = 'chapter_10/favoritenum.json'

def get_favorite_number():
    favorite_number = input('Enter your favorite number: ')
    with open(filename, 'w') as file_obj:
        json.dump(favorite_number, file_obj)

def read_favorite_number():
    with open(filename, 'r') as file_obj:
        favorite_number = json.load(file_obj)
    return favorite_number

def display_favorite_number():
    fav = read_favorite_number()
    print(fav)

try:
    read_favorite_number()
except FileNotFoundError:
    get_favorite_number()
else:
    display_favorite_number()