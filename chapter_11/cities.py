def city_country(city, country, population = ''):
    city = str(city).title()
    country = str(country).title()
    population = str(population)
    if population:
        formatted_name = city + ', ' + country + ' - population: ' + population
    else:
        formatted_name = city + ', ' + country
    return formatted_name