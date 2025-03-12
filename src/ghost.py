from enum import Enum
from character import *
from pacman import *
from algo.search import *
from defs import *
import util
import math

# Define states of a ghost
class GhostState(Enum):
    IDLE = 0 # Doing absolutely nothing
    REST = 1 # Resting in the cage, moving up and down
    WONDER = 2 # Move around randomly, doing random stuff
    TARGETED = 3 # Rush toward pacman, targeted hunting
    RUN_AWAY = 4 # Run away from pacman

class Ghost(Characters):
    state = GhostState.IDLE
    algo_id = -1
    id = -1
    succ = [-1, -1]
    canMove = False
    def __init__(self, _pos, _id, _algo_id):
        super().__init__(_pos)  # Call Character's constructor
        self.state = GhostState.TARGETED # TODO: switch to IDLE
        self.id = _id
        self.algo_id = _algo_id
        self.succ = [-1, -1]
        self.veloc = 1/8
    def update_pos(self):
        if self.pos[0] < self.succ[0]:
            self.pos[0] += self.veloc
        elif self.pos[0] > self.succ[0]:
            self.pos[0] -= self.veloc
        elif self.pos[1] < self.succ[1]:
            self.pos[1] += self.veloc
        elif self.pos[1] > self.succ[1]:
            self.pos[1] -= self.veloc
    def canFindSucc(self, pacman_pos):
        if self.pos[0] % 1.0 == 0 and self.pos[1] % 1.0 == 0:
            if pacman_pos[0] % 1.0 == 0 and pacman_pos[1] % 1.0 == 0:
                return True
        return False
    def move(self, mp, ghosts_pos, pacman_pos):
        if self.canFindSucc(pacman_pos):
            self.succ = Search.get_optimal_successor(self.algo_id, mp, ghosts_pos, self.id, pacman_pos)
            if self.succ == []:
                return
            self.update_pos()
        else:
            self.update_pos()

class Pinky(Ghost):
    def __init__(self, _pos, _id, _algo_id):
        super().__init__(_pos, _id, _algo_id)  
        
class Blinky(Ghost):
    def __init__(self, _pos, _id, _algo_id):
        super().__init__(_pos, _id, _algo_id)  
        
class Inky(Ghost):
    def __init__(self, _pos, _id, _algo_id):
        super().__init__(_pos, _id, _algo_id)  
        
class Clyde(Ghost):
    def __init__(self, _pos, _id, _algo_id):
        super().__init__(_pos, _id, _algo_id)  


        
    
