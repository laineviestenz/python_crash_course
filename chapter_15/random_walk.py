from random import choice
import matplotlib.pyplot as plt

class RandomWalk:
    """a class to generate random walks"""

    def __init__(self, num_points = 5000):
        """initialize attributes of a walk."""
        self.num_points = num_points
        #all walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]
        #define and set default direction values
        self.xdirection = [1, -1]
        self.ydirection = [1, -1]
        #define and set default distance values
        self.xdistance = [0,1,2,3,4]
        self.ydistance = [0,1,2,3,4]

    def set_x_direction(self, xdirection):
        self.xdirection = xdirection

    def set_y_direction(self, ydirection):
        self.ydirection = ydirection

    def set_x_distance(self, xdistance):
        self.xdistance = xdistance

    def set_y_distance(self, ydistance):
        self.ydistance = ydistance

    def fill_walk(self):
        """calculate all the points in the walk"""

        #keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:
            
            #decide which direction to go, and how far to go
            x_direction = choice(self.xdirection)
            x_distance = choice(self.xdistance)
            x_step = x_direction * x_distance

            y_direction = choice(self.ydirection)
            y_distance = choice(self.ydistance)
            y_step = y_direction * y_distance

            #reject moves that go no where
            if x_step == 0 and y_step == 0:
                continue

            #calculate new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            
            self.x_values.append(x)
            self.y_values.append(y)

    def showplot(self):
        """plot the random walk as a scatter plot"""
        #plot the points in the walk
        plt.style.use('classic')
        fig, ax = plt.subplots(figsize=(15,9))
        point_numbers = range(self.num_points)
        ax.scatter(self.x_values, self.y_values, s=15, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none')
        ax.set_aspect('equal')
        #the points could also be set to 0,0 since that is always the starting point, this
        #way just offers backup incase we change the rw funciton
        ax.scatter(self.x_values[0], self.y_values[0], c='green', edgecolors='none', s=100)
        ax.scatter(self.x_values[-1], self.y_values[-1], c='red', edgecolors='none', s=100)
        plt.show()

    def plotwithlines(self, color='blue'):
        """graph the points in the walk, connected by a line"""
        plt.style.use('classic')
        fig, ax = plt.subplots(figsize=(15,9))
        point_numbers = range(self.num_points)
        ax.plot(self.x_values, self.y_values, c=color)
        ax.set_aspect('equal')
        #the starting points could also be set to 0,0 since that is always the 
        #starting point, this way is just more reliable
        ax.scatter(self.x_values[0], self.y_values[0], c='green', s=100)
        ax.scatter(self.x_values[-1], self.y_values[-1], c='red', s=100)
        plt.show()