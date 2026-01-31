import matplotlib.pyplot as plt
from random_walk import RandomWalk

"""I'm changing the excercise slightly here, rather than changing the random
walk class, I am going to create a new method to plot the graph as requested."""

#make a random walk
rw = RandomWalk(5000)
rw.fill_walk()

rw.plotwithlines()