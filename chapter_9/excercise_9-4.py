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

restaurant = Restaurant('McDonalds', 'junk food')
print(restaurant.number_served)

restaurant.set_number_served(0)
print(restaurant.number_served)

restaurant.increment_number_served(45)
print(restaurant.number_served)