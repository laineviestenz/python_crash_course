"""This is pretty much the same as the original excercise 10-5, except that the file is opened in
write mode, which means that each response is stored in a list and then written to the file with
a for loop"""

file_name = 'chapter_10/poll_responses.txt'
response = ''
responses = []

#collect responses and 
while response != 'x':
    response = input('Why do you like programming? ').lower()
    #break loop before appending so 'x' is not written to file
    if response == 'x':
        break
    responses.append(response)

#open the file in write mode after all responses were collected, and itterate through
#the list to make sure all responses are included and not overwritten
with open(file_name, 'w') as file_object:
    for item in responses:
        file_object.write(item + '\n')