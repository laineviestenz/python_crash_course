rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'yelllow river': 'china'
}
for river, country in rivers.items():
    print(river.title() + " runs through " + country.title() + ".")

for i in rivers:
    print(i)

for x in rivers.values():
    print(x)