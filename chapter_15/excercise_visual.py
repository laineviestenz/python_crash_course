from random_walk import RandomWalk
from displayclass import DisplayRW

#make a random walk
rw = RandomWalk(50000)
rw.fill_walk()

DisplayRW.showplot(rw)