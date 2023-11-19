from random import randint

class Die:
    def __init__(self):
        self.sides = 6 # die has 6 sides
    
    def roll_die(self):
        return randint(1, 6)
