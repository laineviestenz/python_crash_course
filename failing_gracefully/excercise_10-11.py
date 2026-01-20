import json
"""stores favorite number in a json"""
favorite_number = input('Enter your favorite number:')

filename = 'chapter_10/favnum.json'
with open(filename, 'w') as file_object:
    json.dump(favorite_number, file_object)