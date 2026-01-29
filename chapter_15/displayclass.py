import matplotlib.pyplot as plt
"""create a class to display the graph. I will commit this for the record, but
I have now realized this would be much better done as a method in the 
randomwalk.py class"""
class DisplayRW():
    def showplot(walkname):
        #plot the points in the walk
        plt.style.use('classic')
        fig, ax = plt.subplots(figsize=(15,9))
        point_numbers = range(walkname.num_points)
        ax.scatter(walkname.x_values, walkname.y_values, s=15, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none')
        ax.set_aspect('equal')
        #the points could also be set to 0,0 since that is always the starting point, this
        #way just offers backup incase we change the rw funciton
        ax.scatter(walkname.x_values[0], walkname.y_values[0], c='green', edgecolors='none', s=100)
        ax.scatter(walkname.x_values[-1], walkname.y_values[-1], c='red', edgecolors='none', s=100)
        plt.show()