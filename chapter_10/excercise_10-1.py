file_name = 'chapter_10/learning_python.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

i = file_object.read()
print(i)

for line in lines:
    print(line.strip())