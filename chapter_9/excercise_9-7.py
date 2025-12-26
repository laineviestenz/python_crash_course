class User():
    def __init__(self, first_name, last_name, age, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.weight = weight
        self.login_attempts = 0

    def increment_login_attempts(self, increment = 1):
        #increases the login attempt, default is 1, but can be adjusted
        #this feature might be handy in a real application
        self.login_attempts += increment

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_person(self):
        """describes the person by first and last name, gives age, weight, and login attempts,
        does not include a description of privieges (see show_priviliges)"""
        print(self.first_name + ' ' + self.last_name + ' is ' + self.age + 
            ' years old and weighs ' + self.weight + ' pounds. ' +
            'He has ' + str(self.login_attempts) + ' login attempts.') 

class Admin(User):
    def __init__(self, first_name, last_name, age, weight):
        super().__init__(first_name, last_name, age, weight)
        self.privileges = ['add post', 'delete post', 'ban user', 'delete account']

    def show_privileges(self):
        """displays the person's full name and lists their privileges with proper grammer in sentence format"""
        print(self.first_name.title() + ' ' + self.last_name.title() + ' can ', end = '')
        for i in self.privileges[:-1]:
            print(i, end = ', ')
        print('and ' + self.privileges[-1] + '.')

# # make a sample of an admin account
admin = Admin('laine', 'viestenz', 5624, 54)
# #display the privileges the admin has
Admin.show_privileges(admin)