import matplotlib.pyplot as plt

#need to plot input and output values otherwise, python assumes x = 0 for first value
input_values = range (1, 1000)
squares = [x ** 2 for x in input_values]

#define prebuilt style to use
plt.style.use('seaborn-v0_8')
#creates a figure, and a set of axes named ax within it
fig, ax = plt.subplots()
#plots the squares information
ax.scatter(input_values, squares, c = squares, cmap=plt.cm.Reds, s = 10)
#configure other aspects of the graph
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)
ax.tick_params (labelsize = 14)

#prints the graph
plt.show()