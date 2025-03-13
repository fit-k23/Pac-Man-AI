from unittest import case

import pygame
import math
from defs import *

# THICKNESS
THICKNESS = 4

class Map:
    data = []
    @staticmethod
    def parse(file_path: str):
        _map = Map()
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                r_line = line.strip('\n').replace(" ", "")
                _map.data.append(r_line)
        return _map

    def draw_grid(self, screen, screen_width, screen_height, block_width, block_height):
        for x in range(0, screen_width, block_width):
            for y in range(0, screen_height, block_height):
                rect = pygame.Rect(x, y, block_width, block_height)
                pygame.draw.rect(screen, WHITE, rect, 1)

    def get_character_pos(self):
        pacman = [0, 0]
        ghosts = []
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i][j] == 'p':
                    pacman = [j, i]
                elif self.data[i][j] == 'g':
                    ghosts.append([j, i])
        return pacman, ghosts

    def get_food_pos(self):
        food = []
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i][j] == '1':
                    food.append((i, j))

        return food

    def draw_map(self, screen, screen_width, screen_height, block_width, block_height):
        off_x = 1
        off_y = 1
        off_block = 2
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                x = j * block_width
                y = i * block_height
                # 5, 6, 7, 8: arc
                if self.data[i][j] == '5':
                    rect = pygame.Rect(x - block_width / 2 + off_x, y + block_height / 2 - off_y, block_width + off_block, block_height + off_block)
                    pygame.draw.arc(screen, BLUE, rect, math.radians(0), math.radians(90), THICKNESS)
                elif self.data[i][j] == '6':
                    rect = pygame.Rect(x + block_width / 2 - off_x, y + block_height / 2 - off_y, block_width + off_block, block_height + off_block)
                    pygame.draw.arc(screen, BLUE, rect, math.radians(90), math.radians(180), THICKNESS)
                elif self.data[i][j] == '7':
                    rect = pygame.Rect(x + block_width / 2 - off_x, y - block_height / 2 + off_y, block_width + off_block, block_height + off_block)
                    pygame.draw.arc(screen, BLUE, rect, math.radians(180), math.radians(270), THICKNESS)
                elif self.data[i][j] == '8':
                    rect = pygame.Rect(x - block_width / 2 + off_x, y - block_height / 2 + off_y, block_width + off_block, block_height + off_block)
                    pygame.draw.arc(screen, BLUE, rect, math.radians(270), math.radians(360), THICKNESS)
                # 3, 4: straight line
                elif self.data[i][j] == '3':
                    start_pos = (x + block_width / 2, y)
                    end_pos = (x + block_width / 2, y + block_height)
                    pygame.draw.line(screen, BLUE, start_pos, end_pos, THICKNESS)
                elif self.data[i][j] == '4':
                    start_pos = (x, y + block_height / 2)
                    end_pos = (x + block_width, y + block_height / 2)
                    pygame.draw.line(screen, BLUE, start_pos, end_pos, THICKNESS)


    def draw_food(self, screen, block_width, block_height, food_pos):
        for (col, row) in food_pos:
            x = row * block_width
            y = col * block_height
            centerPos = (x + block_width / 2, y + block_height / 2)
            radius = block_width / 4
            pygame.draw.circle(screen, YELLOW, centerPos, radius)

    def erase_food(self, food_pos, x, y):
        if (x, y) in food_pos:
            food_pos.remove((x, y))







