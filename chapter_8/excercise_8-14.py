def car_profile(manufacture, mod, **details):
    car_id = {}
    car_id['manufacturer'] = manufacture
    car_id['model'] = mod
    for key, value in details.items():
        car_id[key] = value
    print(car_id)

car_profile('audi', 'A5', color = 'black', transmission = 'shot')