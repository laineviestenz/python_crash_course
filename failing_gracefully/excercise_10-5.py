file_name = 'chapter_10/poll_responses.txt'
response = ''

while response != 'x':
    if response == 'x':
        break
    response = input('Why do you like programming? ').lower()
    with open(file_name, 'a') as file_object:
        file_object.write(response + '\n')