import pygame
import math
from color import *

# THICKNESS
THICK = 4

class Map:
    data = []
    @staticmethod
    def parse(file_path: str):
        _map = Map()
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                str = line.strip('\n').replace(" ", "")
                _map.data.append(str)
        return _map
    def drawGrid(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE):
        for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
            for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
                rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(screen, WHITE, rect, 1)
    def drawMap(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE):
        off_x = 1
        off_y = 1
        off_block = 2
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                x = j * BLOCK_SIZE
                y = i * BLOCK_SIZE
                # 5, 6, 7, 8: arc
                if self.data[i][j] == '6':
                    rect = pygame.Rect(x + BLOCK_SIZE / 2 - off_x, y + BLOCK_SIZE / 2 - off_y, BLOCK_SIZE + off_block, BLOCK_SIZE + off_block)
                    pygame.draw.arc(screen, BLUE, rect, math.radians(90), math.radians(180), THICK)
                elif self.data[i][j] == '8':
                    rect = pygame.Rect(x - BLOCK_SIZE / 2 + off_x, y - BLOCK_SIZE / 2 + off_y, BLOCK_SIZE + off_block, BLOCK_SIZE + off_block)
                    pygame.draw.arc(screen, BLUE, rect, math.radians(270), math.radians(360), THICK)
                elif self.data[i][j] == '5':
                    rect = pygame.Rect(x - BLOCK_SIZE / 2 + off_x, y + BLOCK_SIZE / 2 - off_y, BLOCK_SIZE + off_block, BLOCK_SIZE + off_block)
                    pygame.draw.arc(screen, BLUE, rect, math.radians(0), math.radians(90), THICK)
                elif self.data[i][j] == '7':
                    rect = pygame.Rect(x + BLOCK_SIZE / 2 - off_x, y - BLOCK_SIZE / 2 + off_y, BLOCK_SIZE + off_block, BLOCK_SIZE + off_block)
                    pygame.draw.arc(screen, BLUE, rect, math.radians(180), math.radians(270), THICK)
                # 3, 4: straight line
                elif self.data[i][j] == '3':
                    startPos = (x + BLOCK_SIZE / 2, y)
                    endPos = (x + BLOCK_SIZE / 2, y + BLOCK_SIZE)
                    pygame.draw.line(screen, BLUE, startPos, endPos, THICK)
                elif self.data[i][j] == '4':
                    startPos = (x, y + BLOCK_SIZE / 2)
                    endPos = (x + BLOCK_SIZE, y + BLOCK_SIZE / 2)
                    pygame.draw.line(screen, BLUE, startPos, endPos, THICK)