import matplotlib.pyplot as plt
from random_walk import RandomWalk

"""Change the options that the random walk chooses between"""

#make a random walk
rw = RandomWalk(5000)
#change the options for the direction and distance
rw.set_x_direction([1, -1])
rw.set_y_direction([1, -1])
rw.set_x_distance([0,1,2,3,4])
rw.set_y_distance([0,1])

#generate the values
rw.fill_walk()

#uses optional color input to color lines
rw.showplot()