class Restaurant():
    """define a restaurant and its details"""

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(self.name.title() + ' is a restaurant that serves ' + self.cuisine + ' food.')
    
    def open_restaurant(self):
        print(self.name.title() + ' is open!')

restaurant = Restaurant('China Buffet', 'Chineese')

restaurant.describe_restaurant()
restaurant.open_restaurant()
