active = True
while active:
    topping = input("enter your toppings one at a time, enter quit when finished: ")
    if topping == 'quit':
        active = False
    else:
        print("I will add " + topping + '.')