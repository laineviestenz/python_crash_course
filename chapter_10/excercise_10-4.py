i = ''
file_name = 'chapter_10/guest_book.txt'

print("Please enter each guest's name, type x when finished.")
while i != 'x':
    i = input('Please enter guest name: ').lower()
    if i == 'x':
        break
    print('Welcome, ' + i.title())
    with open(file_name, 'a') as file_object:
        file_object.write(i.title() + '\n')