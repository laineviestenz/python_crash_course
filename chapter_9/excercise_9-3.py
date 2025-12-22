class User():
    def __init__(self, first_name, last_name, age, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.weight = weight
    def describe_person(self):
        print(self.first_name + ' ' + self.last_name + ' is ' + self.age + ' years old and weighs ' + self.weight + ' pounds.') 

santa = User('Santa', 'Clause', '487', '670')
User.describe_person(santa)