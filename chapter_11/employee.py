class Employee():
    def __init__(self, first_name, last_name, salary):
        self.first_name = str(first_name).title()
        self.last_name = str(last_name).title()
        self.salary = salary
    
    def give_raise(self, amount = 5000):
        self.salary += amount

    def get_salary(self):
        return self.salary