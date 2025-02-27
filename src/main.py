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


dl = 0
director = 0


ghost_images = []
ghost_X = 450
ghost_Y = 663
collision_wall = [False, False, False, False]



for i in range (1,2):
    ghost_images.append(pygame.transform.scale(pygame.image.load(f'/Users/nguyentienluat/Documents/GitHub/Pac-Man-AI/pic/{1}.png'), (80, 80)))
    
def draw_ghost():
    if director == 0:
        screen.blit(ghost_images[0], (ghost_X, ghost_Y))
    if director == 1:
        screen.blit(pygame.transform.flip(ghost_images[0], True, False), (ghost_X, ghost_Y))
    if director == 2:
        screen.blit(pygame.transform.rotate(ghost_images[0], 90), (ghost_X, ghost_Y))
    if director == 3:
        screen.blit(pygame.transform.rotate(ghost_images[0], 270), (ghost_X, ghost_Y))


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
    
    
    draw_ghost()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        director = 2
        ghost_Y -= 300 * dt
    if keys[pygame.K_s]:
        director = 3
        ghost_Y += 300 * dt
    if keys[pygame.K_d]:
        director = 0
        ghost_X += 300 * dt
    if keys[pygame.K_a]:
        director = 1
        ghost_X -= 300 * dt

    # for i in range(len(maze.data)):
    #     for j in range(len(maze.data[i])):
    #         print(maze.data[i][j], end="")
    #     print()
    # break

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000 # limits FPS to 60

pygame.quit()
