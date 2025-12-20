def describe_city(name, country = ' the united states'):
    print(name + ' is in ' + country + '.')

describe_city('San Diego')
describe_city('New York City')
describe_city('Ontario', country = 'canada')