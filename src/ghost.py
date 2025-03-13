from enum import Enum
from pacman import *
from search import *

from map import Map

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
    successor = [-1, -1]
    canMove = False
    algo_path = []
    algo_upd_cnt = -1
    algo_upd_limit = 0
    pacman_changing = 0
    pacman_prev_pos = [-1, -1]

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
        self.pacman_prev_pos = [-1, -1]

    # Move toward successor
    def update_pos(self):
        if self.pos[0] < self.successor[0]:
            self.pos[0] += self.velocity
        elif self.pos[0] > self.successor[0]:
            self.pos[0] -= self.velocity
        elif self.pos[1] < self.successor[1]:
            self.pos[1] += self.velocity
        elif self.pos[1] > self.successor[1]:
            self.pos[1] -= self.velocity

    # update new path for ghost
    def update_path(self, _map, ghosts_pos, pacman_pos, forbid = []):
        self.algo_path = Search.get_path(self.algo_id, _map, ghosts_pos, self.id, pacman_pos, forbid)
        self.algo_upd_limit = len(self.algo_path) - 1
        self.algo_upd_cnt = 0

    # If another ghost is in the successor, re-update the path with the forbidden successor
    # Only apply to dfs and bfs, A* and UCS avoid ghost-colliding before return successor
    def update_collide_path(self, _map, ghosts_pos, pacman_pos):
        if 1 <= self.id <= 2:
            while True:
                collide_pos = self.collide(ghosts_pos, self.algo_path[self.algo_upd_cnt])
                if collide_pos == []:
                    break
                # Pass collide successor to enable randomly chosen successor
                self.update_path(_map, ghosts_pos, pacman_pos, collide_pos)

    # Check if any ghost in successor
    def collide(self, ghosts_pos, pos):
        eps = 0.9
        for i in range(4):
            if i != self.id:
                if math.fabs(ghosts_pos[i][0] - pos[0]) <= eps and math.fabs(ghosts_pos[i][1] - pos[1]) <= eps:
                    return ghosts_pos[i]
        return []

    # Check if eat pacman
    @staticmethod
    def eat_pacman(ghosts_pos, pacman_pos):
        eps = 0.6
        for i in range(4):
            if math.fabs(ghosts_pos[i][0] - pacman_pos[0]) <= eps and math.fabs(ghosts_pos[i][1] - pacman_pos[1]) <= eps:
                return True
        return False

    # Get the next successor
    def get_next_successor(self, _map, ghosts_pos, pacman_pos):
        if self.pos[0] % 1.0 == 0 and self.pos[1] % 1.0 == 0 and pacman_pos[0] % 1.0 == 0 and pacman_pos[1] % 1.0 == 0:
            if self.algo_upd_cnt == -1 or self.algo_upd_cnt >= self.algo_upd_limit or self.pacman_changing == 5:
                self.update_path(_map, ghosts_pos, pacman_pos)
                self.update_collide_path(_map, ghosts_pos, pacman_pos)
                return self.algo_path[self.algo_upd_cnt]
            elif self.algo_upd_cnt < self.algo_upd_limit:
                self.algo_upd_cnt += 1
                self.update_collide_path(_map, ghosts_pos, pacman_pos)
                return self.algo_path[self.algo_upd_cnt]
        return self.successor

    # Move the ghost
    def move(self, _map: Map, ghosts_pos, pacman_pos):    
        if pacman_pos[0] % 1.0 == 0 and pacman_pos[1] % 1.0 == 0:
            if self.pacman_prev_pos == [-1, -1]:
                self.pacman_prev_pos = pacman_pos
            else:
                if self.pacman_prev_pos != pacman_pos:
                    self.pacman_changing = (self.pacman_changing + 1) % 6
                self.pacman_prev_pos = pacman_pos
        self.successor = self.get_next_successor(_map, ghosts_pos, pacman_pos)
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


        
    
