import matplotlib.pyplot as plt
from chapter_15.rw_modified import RandomWalk

"""I'm changing the excercise slightly here, rather than changing the random
walk class, I am going to create a new method to plot the graph as requeste."""

#make a random walk
rw = RandomWalk(500)
rw.fill_walk()

#plot the points in the walk
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15,9))
point_numbers = range(rw.num_points)
ax.plot(rw.x_values, rw.y_values, linewidth=1)
ax.set_aspect('equal')
#the points could also be set to 0,0 since that is always the starting point, this
#way just offers backup incase we change the rw funciton
ax.scatter(rw.x_values[0], rw.y_values[0], c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
plt.show()

