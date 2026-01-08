class Restaurant():
    """define a restaurant and its details"""

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0
    
    def set_number_served(self, customers_served):
        self.number_served = customers_served

    def increment_number_served(self, customers_served):
        self.number_served += customers_served

    def describe_restaurant(self):
        print(self.name.title() + ' is a restaurant that serves ' + self.cuisine + ' food.')
    
    def open_restaurant(self):
        print(self.name.title() + ' is open!')

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors = ['vanilla', 'chocolate']):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def get_flavors(self):
        for i in self.flavors:
            print(i)
        print('')
    
    def update_flavors(self, new_flavors):
        ''' Takes the name of the icecream stand to be updated and the new list of flavors'''
        self.flavors = new_flavors