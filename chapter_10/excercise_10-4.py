input = ''
file_name = 'chapter_10/guest_book.txt'

while input != 'x':
    input = input('Please enter guest name: ')
    print('Welcome, ' + input)
    with open(file_name) as file_object:
        file_object.write(input + '\n')