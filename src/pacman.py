from map import *
from character import *
from defs import *

# Direction: 0 - up, 1 - down, 2 - left, 3 - right
class Pacman(Characters):
    score = 0
    def __init__(self, _pos):
        super().__init__(_pos)  # Call Character's constructor
        self.score = 0

    # Move the pacman and eat food
    def move(self, mp, food_pos):
        offset_check_turn = 0.9
        # If there are keyboard pressed (W, S, A, D)
        if self.last_request != -1:
            # Check if pacman can teleport
            if self.teleport(mp, self.last_request, True):
                return
            if self.last_request == 0:
                if can_go([self.pos[0], math.floor(self.pos[1] - self.velocity)], mp) and self.pos[0] % 1.0 == 0:
                    self.prev_pos = self.pos
                    self.pos[1] -= self.velocity
                    self.update_dir()
                    return
            elif self.last_request == 1:
                if can_go([self.pos[0], math.floor(self.pos[1] + offset_check_turn + self.velocity)], mp) and self.pos[0] % 1.0 == 0:
                    self.prev_pos = self.pos
                    self.pos[1] += self.velocity
                    self.update_dir()
                    return
            elif self.last_request == 2:
                if can_go([math.floor(self.pos[0] - self.velocity), self.pos[1]], mp) and self.pos[1] % 1.0 == 0:
                    self.prev_pos = self.pos
                    self.pos[0] -= self.velocity
                    self.update_dir()
                    return
            elif self.last_request == 3:
                if can_go([math.floor(self.pos[0] + offset_check_turn + self.velocity), self.pos[1]], mp) and self.pos[1] % 1.0 == 0:
                    self.prev_pos = self.pos
                    self.pos[0] += self.velocity
                    self.update_dir()
                    return

        # If the code can reach here, then there are either no requests or the last request can't be performed.
        # So we keep moving current direction (if possible).

        # Check if pacman can teleport
        if self.teleport(mp, self.dir, False):
            return

        if self.dir == 0:
            if can_go([self.pos[0], math.floor(self.pos[1] - self.velocity)], mp) and self.pos[0] % 1.0 == 0:
                self.prev_pos = self.pos
                self.pos[1] -= self.velocity
        elif self.dir == 1:
            if can_go([self.pos[0], math.floor(self.pos[1] + offset_check_turn + self.velocity)], mp) and self.pos[0] % 1.0 == 0:
                self.prev_pos = self.pos
                self.pos[1] += self.velocity
        elif self.dir == 2:
            if can_go([math.floor(self.pos[0] - self.velocity), self.pos[1]], mp) and self.pos[1] % 1.0 == 0:
                self.prev_pos = self.pos
                self.pos[0] -= self.velocity
        elif self.dir == 3:
            if can_go([math.floor(self.pos[0] + offset_check_turn + self.velocity), self.pos[1]], mp) and self.pos[1] % 1.0 == 0:
                self.prev_pos = self.pos
                self.pos[0] += self.velocity

        if mp.erase_food(food_pos, int(self.pos[1]), int(self.pos[0])):
            self.score += 1
        
