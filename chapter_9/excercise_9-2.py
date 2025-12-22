class Restaurant():
    """define a restaurant and its details"""

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(self.name.title() + ' is a restaurant that serves ' + self.cuisine + '.')
    
    def open_restaurant(self):
        print(self.name.title() + ' is open!')

chineese_buffet = Restaurant('China Buffet', 'Chineese')
little_ceasers = Restaurant('little ceasers', 'pizza')
taco_bell = Restaurant('Taco bell', 'tacos')

chineese_buffet.describe_restaurant()
little_ceasers.describe_restaurant()
taco_bell.describe_restaurant()