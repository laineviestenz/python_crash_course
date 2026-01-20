"""This file takes the 10-1 excercise and conducts an experiment where I replace
words by turning the list into a string"""

file_name = 'chapter_10/learning_python.txt'

with open(file_name) as file_object:
    """read and print the entire document"""
    full_version = file_object.read()
    print(full_version)
    
with open(file_name) as file_object:
    """read and print line by line"""
    lines = file_object.readlines()
    for line in lines:
        print(line.strip())

with open(file_name) as file_object:
    """create a list of each line and print it outside the with statment"""
    lines = file_object.readlines()
    list_items = []
    for item in lines:
        list_items.append(item)

#print the full list
print(list_items)

#create a new varaible that is the string of the list so we can replace
#words without losing the original list and its functionality
abilities = str(list_items)
print(abilities.replace('python', 'c'))

#check the original list works
list_items.append('in python you can save files')
print(list_items)