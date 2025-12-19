sandwich_orders = ["sub", 'cheese', 'goat', 'sub', 'sub',  'ham', 'turkey']
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop(0)
    finished_sandwiches.append(order)
    print('I am making your ' + order + ' sandwich')

i = set(finished_sandwiches)

print("We have made ", end = '')
for sandwich in i:
    print(sandwich, end = ', ')
print('sandwiches.')