psmith = {
    "first_name": "Peter", 
    "last_name": "Smith", 
    "age": "105843 years old",
    "city": "NYC"
    }

gcooper = {
    "first_name": "Georgie",
    "last_name": "Cooper",
    "age": "not 17",
    "city": "Austin"
}

mdawg = {
    "first_name": "Mil",
    "last_name": "Dawg",
    "age": "22",
    "city": "San Diego"
}

people = [psmith, gcooper, mdawg]

for person in people:
    print('First Name: ' + person["first_name"].title())
    print('Last Name: ' + person["last_name"].title())
    print('age: ' + person["age"])
    print('city: ' + person["city"].title() + "\n")