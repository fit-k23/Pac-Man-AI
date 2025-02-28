import pygame
import math
from color import *
from map import *

# Direction: 0 - up, 1 - down, 2 - left, 3 - right
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
class PacMan:
    pos = [0, 0] # positon on map
    dir = 0 # current direction
    delay = 0 # delay for slow movement
    last_request = -1 # save the last request to change direction
    # Constructor
    def __init__(self, _pos):
        self.pos = _pos
        self.dir = 0
        self.last_request = -1

    # Check if a block can be reached by characters
    def can_go(self, check_pos, mp): 
        # TODO: update teleport if out of map
        if check_pos[0] < 0 or check_pos[0] >= 30 or check_pos[1] < 0 or check_pos[1] >= 33:
            return False
        if mp[check_pos[1]][check_pos[0]] >= '3' and mp[check_pos[1]][check_pos[0]] <= '8':
            return False
        return True 

    # Get new position (parameter d: direction)
    def get_new_pos(self, d):
        new_pos = [self.pos[0], self.pos[1]]
        if d == 0: 
            if new_pos[1] == 0:
                new_pos[1] = 32
            else:
                new_pos[1] -= 1
        elif d == 1:
            if new_pos[1] == 32:
                new_pos[1] = 0
            else:
                new_pos[1] += 1
        elif d == 2:
            if new_pos[0] == 0:
                new_pos[0] = 29
            else:
                new_pos[0] -= 1
        else:
            if new_pos[0] == 29:
                new_pos[0] = 0
            else:
                new_pos[0] += 1
        return new_pos

    # Move the pacman along blocks
    def move(self, mp):
        if self.last_request == -1:
            new_pos = self.get_new_pos(self.dir)
            if self.can_go(new_pos, mp):
                self.pos = new_pos
        else:
            new_pos = self.get_new_pos(self.last_request)
            if self.can_go(new_pos, mp):
                self.pos = new_pos
                self.dir = self.last_request
                self.last_request = -1
            else:
                new_pos = self.get_new_pos(self.dir)
                if self.can_go(new_pos, mp):
                    self.pos = new_pos
            
    # Draw pacman
    def draw(self, screen, BLOCK_W, BLOCK_H):
        rect = pygame.Rect(self.pos[0] * BLOCK_W, self.pos[1] * BLOCK_H, BLOCK_W, BLOCK_H)
        pygame.draw.rect(screen, YELLOW, rect)