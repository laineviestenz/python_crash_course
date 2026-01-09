from random import randint
class Die():
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_dice(self):
        x = randint(1, self.sides)
        print(x)

regular = Die()
regular.roll_dice()

deca = Die(10)
deca.roll_dice()