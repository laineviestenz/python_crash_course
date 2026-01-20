"""open and print a file that contains cat and dog names, print an error message
if the file cannot be found"""

cats_file = 'chapter_10/cat.txt'
dogs_file = 'chapter_10/dogs.txt'

print('\ndog names:')
try:
    with open(cats_file, 'r') as cats_object:
        cats = cats_object.read()
except FileNotFoundError:
    print('sorry, file not found')
else:
    print(cats)

print('\ncat names:')
try:
    with open(dogs_file, 'r') as dogs_object:
        dogs = dogs_object.read()
except FileNotFoundError:
    print('Sorry, the file could not be found.')
else:
    print(dogs)