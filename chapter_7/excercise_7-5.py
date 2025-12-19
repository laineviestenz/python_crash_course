while True:
    age = input("Enter age, enter quit to quit: " )
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            price = 0
        elif age < 12 or age > 65:
            price = 10
        else:
            price = 15
    print ('Your price is: $' + str(price))