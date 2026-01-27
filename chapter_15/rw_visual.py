import matplotlib.pyplot as plt

from random_walk import RandomWalk

#make a random walk
rw = RandomWalk()
rw.fill_walk()

#plot the points in the walk
plt.style.use('classic')
fig, ax = plt.subplots()
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, s=15, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none')
ax.set_aspect('equal')

plt.show()
