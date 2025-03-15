import pygame

class Texture:
    pause: bool
    def __init__(self, frames):
        self.__texture_index = 0
        self.frames = frames

    def pause(self):
        pause = True

    def unpause(self):
        pause = False

    def reset(self):
        self.__texture_index = -1
        self.__last_update = pygame.time.get_ticks()
        self.__animation_speed = 50