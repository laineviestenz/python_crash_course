"""this is a program that takes a text document in the same folder, saves it
with the variable file_name and then uses three different methods to work with
and print the list. Note that each method requires its own with statement to 
open and read the file, or else it becomes inaccessible."""

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

print(list_items)