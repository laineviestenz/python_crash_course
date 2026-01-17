"""appends guest names to list one at a time. Future improvement
option might be to store guests in a list and append them when some
sort of exit code is typed."""

file_name = 'chapter_10/guests.txt'

with open(file_name, 'a') as file_object:
    guest = input('Enter guest name: ')
    file_object.write(guest + '\n')