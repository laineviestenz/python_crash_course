from random import randint

class Die():
    """creates a die with a default value of six sides, but can be updated to 
    any size"""
    
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_dice(self):
        """chooses a random integer between 1 and the number of sides defined."""
        x = randint(1, self.sides)
        print(x)

#default 6 sided die
regular = Die()
regular.roll_dice()

#10 sided die
deca = Die(10)
deca.roll_dice()