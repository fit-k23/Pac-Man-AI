from enum import Enum
from pacman import *
from search import *

from map import Map

# Define states of a ghost
class GhostState(Enum):
    IDLE = 0 # Doing absolutely nothing
    REST = 1 # Resting in the cage, moving up and down
    WANDER = 2 # Move around randomly, doing random stuff
    TARGETED = 3 # Rush toward pacman, targeted hunting
    RUN_AWAY = 4 # Run away from pacman

class Ghost(Characters):
    state = GhostState.IDLE
    algo_id = -1 # algorithm id for the ghost
    id = -1 # ghost id
    successor = [-1, -1] # next step to move
    algo_path = [] # Current path to reach pacman
    algo_upd_cnt = -1 # Iterator of the array algo_path[]
    algo_upd_limit = 0 # Limit of the iterator
    pacman_prev_pos = [-1, -1] # Keep track of pacman's previous position

    # Ghost constructor
    def __init__(self, _pos, _id, _algo_id):
        super().__init__(_pos)  # Call Character's constructor
        self.state = GhostState.TARGETED # TODO: switch to IDLE
        self.id = _id
        self.algo_id = _algo_id
        self.successor = [-1, -1]
        self.velocity = 1 / 8
        self.algo_path = []
        self.algo_upd_limit = -1
        self.algo_upd_cnt = -1
        self.pacman_changing = 0
        self.pacman_pre_upd = [-1, -1]

    # Move toward successor - only 1 block move
    def update_pos(self):
        if self.successor is None:
            return
        if self.pos[0] < self.successor[0]:
            self.pos[0] += self.velocity
        elif self.pos[0] > self.successor[0]:
            self.pos[0] -= self.velocity
        elif self.pos[1] < self.successor[1]:
            self.pos[1] += self.velocity
        elif self.pos[1] > self.successor[1]:
            self.pos[1] -= self.velocity

    # Update the new path for ghost
    def update_path(self, _map, ghosts_pos, pacman_pos, succ_list):
        self.pacman_pre_upd = pacman_pos
        self.algo_path = Search.get_path(self.algo_id, _map, ghosts_pos, self.id, pacman_pos, succ_list)
        self.algo_upd_cnt = 0
        self.algo_upd_limit = len(self.algo_path) - 1

    def pacman_far_enough(self, pacman_pos):
        if self.pacman_pre_upd != [-1, -1] and abs(pacman_pos[0] - self.pacman_pre_upd[0]) + abs(pacman_pos[1] - self.pacman_pre_upd[1]) == 5:
            return True
        return False

    # Get the next successor
    def get_next_successor(self, _map, ghosts_pos, succ_list, pacman_pos):
        # Only get new successor if the ghost is inside the block
        if self.pos[0] % 1.0 == 0 and self.pos[1] % 1.0 == 0:
            # Can update new path if pacman is inside block
            if self.algo_upd_cnt == -1 or self.algo_upd_cnt == self.algo_upd_limit or self.pacman_far_enough(pacman_pos):
                if pacman_pos[0] % 1.0 == 0 and pacman_pos[1] % 1.0 == 0:
                    # print("Update path")
                    self.update_path(_map, ghosts_pos, pacman_pos, succ_list)
                    return self.algo_path[self.algo_upd_cnt]
            elif self.algo_upd_cnt < self.algo_upd_limit:
                self.algo_upd_cnt += 1
                # print("Next succ without update new path")
                if in_succ_list(succ_list, self.id, self.algo_path[self.algo_upd_cnt]):
                    self.update_path(_map, ghosts_pos, pacman_pos, succ_list)
                    # print("Reupdate new path")
                return self.algo_path[self.algo_upd_cnt]
        # If not able to find next successor, return current successor to move or wait
        return self.successor

    # Move the ghost
    def move(self, _map: Map, ghosts_pos, succ_list, pacman_pos):
        self.successor = self.get_next_successor(_map, ghosts_pos, succ_list, pacman_pos)
        self.update_pos()
    
    # Check if eat pacman
    @staticmethod
    def eat_pacman(ghosts_pos, pacman_pos):
        eps = 0.6
        for i in range(4):
            if math.fabs(ghosts_pos[i][0] - pacman_pos[0]) <= eps and math.fabs(ghosts_pos[i][1] - pacman_pos[1]) <= eps:
                return True
        return False

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


        
    
