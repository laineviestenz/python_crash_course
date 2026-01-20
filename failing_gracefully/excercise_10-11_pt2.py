import json
"""fetches the favorite number stored in the json"""

filename = 'chapter_10/favnum.json'
with open(filename, 'r') as file_object:
    favorite_number = json.load(file_object)

print(favorite_number)