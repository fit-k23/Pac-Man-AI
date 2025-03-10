from map import *
from character import *


# Direction: 0 - up, 1 - down, 2 - left, 3 - right
class Pacman(Characters):
    # Constructor
    def __init__(self, _pos):
        super().__init__(_pos)
    
    def move(self, mp, food_pos):
        super().move(mp)
        mp.delete_food(food_pos, self.pos[1], self.pos[0])
        
