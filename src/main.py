import pygame
from map import Map

# Screen and Block paramters
BLOCK_SIZE = 25
SCREEN_WIDTH = BLOCK_SIZE * 28
SCREEN_HEIGHT = BLOCK_SIZE * 30
OFFSET_BLOCK = 2

# Color 
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

# Map object
maze = Map.parse("../asset/maps/map_02.txt")

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    
    maze.drawGrid(screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE)
    maze.drawMap(screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, OFFSET_BLOCK)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()