from map import *
from util import *

# This is a parent class of pacman and ghosts.
# The move function of pacman and ghosts are different so it is defined in child class.
class Characters:
    pos = [0, 0] # positon on grid (array type []), use (x, y) coordinates in pygame
    prev_pos = [-1, -1] # previous position of character (-1 indicates character has not moved)
    dir = -1 # current moving direction
    delay = 0 # delay for slow movement
    last_request = -1 # save the last request to change direction
    velocity = 1 / 4 # velocity

    # Constructor
    def __init__(self, _pos):
        self.pos = _pos  
        self.prev_pos = [-1, -1]
        self.dir = -1
        self.delay = 0  
        self.last_request = -1 
        self.velocity = 1 / 4

        self.textures = []
        self.__texture_index = -1
        self.__last_update = pygame.time.get_ticks()
        self.__animation_speed = 50  
    
    # Update direction according to last request
    def update_dir(self):
        self.dir = self.last_request
        self.last_request = -1
    
    # Load the textures
    def load_textures(self, texture_list):
        # print(texture_list)
        for texture in texture_list:
            # print(texture)
            image = pygame.image.load(texture)
            self.textures.append(pygame.transform.scale(image, (32, 32)))
            self.__texture_index = 0

    # Update animation            
    def update_animation(self):
        now = pygame.time.get_ticks()
        if now - self.__last_update > self.__animation_speed:
            self.__last_update = now
            self.__texture_index = (self.__texture_index + 1) % len(self.textures)
        
    # Check if character can teleport through map
    def teleport(self, mp, d, is_upd):
        if d == 0:
            if self.pos[0] % 1.0 == 0 and self.pos[1] == 0:
                if can_go([self.pos[0], 32], mp):
                    # self.prev_pos = self.pos
                    self.pos[1] = 32
                    if is_upd:
                        self.update_dir()
                    return True
        elif d == 1:
            if self.pos[0] % 1.0 == 0 and self.pos[1] == 32:
                if can_go([self.pos[0], 0], mp):
                    # self.prev_pos = self.pos
                    self.pos[1] = 0
                    if is_upd:
                        self.update_dir()
                    return True
        elif d == 2:
            if self.pos[1] % 1.0 == 0 and self.pos[0] == 0:
                if can_go([29, self.pos[1]], mp):
                    # self.prev_pos = self.pos
                    self.pos[0] = 29
                    if is_upd:
                        self.update_dir()
                    return True
        elif d == 3:
            if self.pos[1] % 1.0 == 0 and self.pos[0] == 29:
                if can_go([0, self.pos[1]], mp):
                    # self.prev_pos = self.pos
                    self.pos[0] = 0
                    if is_upd:
                        self.update_dir()
                    return True
        return False   

    # Draw character
    def draw(self, screen, block_width, block_height):
        if self.__texture_index == -1:
            return
        self.update_animation()
        image = self.textures[self.__texture_index]
        if self.dir == 0:
            image = pygame.transform.rotate(image, 90)
        elif self.dir == 1:
            image = pygame.transform.rotate(image, -90)
        elif self.dir == 2:
            image = pygame.transform.flip(image, True, False)  # Flip horizontally

        screen.blit(image, ((self.pos[0] - 0.25) * block_width, (self.pos[1] - 0.25) * block_height))
            

