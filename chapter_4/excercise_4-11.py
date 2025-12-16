pizzas = ["cheese", "peperoni", "supreme"]

friend_pizzas = pizzas[:]

pizzas.append('bbq')
friend_pizzas.append("ranch")


print("I like:", end = " ")
for pizza in pizzas[:-1]:
    print(pizza, end = ", ")
print (pizzas[-1], end = ".\n")

print("My friend likes:", end = " ")
for pizza in friend_pizzas[:-1]:
    print(pizza, end = ", ")
print (pizzas[-1], end = ".")