import pygame
from map import *

# Screen, Block paramters
BLOCK_SIZE = 20
SCREEN_WIDTH = BLOCK_SIZE * 30
SCREEN_HEIGHT = BLOCK_SIZE * 33

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
    # maze.drawGrid(screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE)
    maze.drawMap(screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE)

    # for i in range(len(maze.data)):
    #     for j in range(len(maze.data[i])):
    #         print(maze.data[i][j], end="")
    #     print()
    # break

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()