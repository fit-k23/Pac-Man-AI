import pygame

# Color 
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

class Map:
    data = []
    @staticmethod
    def parse(file_path: str):
        _map = Map()
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                _map.data.append([*line.strip('\n')])
        return _map
    def drawGrid(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE):
        for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
            for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
                rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(screen, WHITE, rect, 1)
    def drawMap(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, OFFSET_BLOCK):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i][j] == '*':
                    rect = pygame.Rect(j * BLOCK_SIZE, i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                    pygame.draw.rect(screen, BLUE, rect, 0)
                elif self.data[i][j] == '.':
                    rect = pygame.Rect(j * BLOCK_SIZE + BLOCK_SIZE / 2 - OFFSET_BLOCK, i * BLOCK_SIZE + BLOCK_SIZE / 2 - OFFSET_BLOCK, 5, 5)
                    pygame.draw.rect(screen, RED, rect, 0)