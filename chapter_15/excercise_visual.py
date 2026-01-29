import matplotlib.pyplot as plt

from excercisefifteenfour import RandomWalk

#make a random walk
rw = RandomWalk(50000, xdirection = [-1,1], stepdistance = [0,1,2,3,4,5,6,7,8,9])
rw.fill_walk()

#plot the points in the walk
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15,9))
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, s=15, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none')
ax.set_aspect('equal')
#the points could also be set to 0,0 since that is always the starting point, this
#way just offers backup incase we change the rw funciton
ax.scatter(rw.x_values[0], rw.y_values[0], c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
plt.show()