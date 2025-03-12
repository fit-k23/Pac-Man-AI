import pygame
from map import *
from pacman import *
from ghost import *
from algo import *
from defs import *

# Screen, Block parameters

BLOCK_W = 25
BLOCK_H = 20
SCREEN_WIDTH = BLOCK_W * 30
SCREEN_HEIGHT = BLOCK_H * 33

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

# Map object
maze = Map.parse("../asset/maps/map_02.txt")

# Get position of pacman, ghosts, and food at first
(pacman_pos, ghosts_pos) = maze.get_character_pos()
food_pos = maze.get_food_pos() 
pacman = Pacman(pacman_pos)
ghosts = [Clyde(ghosts_pos[0], CLYDE, CLYDE_ALGO), Pinky(ghosts_pos[1], PINKY, PINKY_ALGO), Inky(ghosts_pos[2], INKY, INKY_ALGO),
          Blinky(ghosts_pos[3], BLINKY, BLINKY_ALGO)]

# Load character's textures
pacman.load_textures([f"../asset/pacman/pacman_{i}.png" for i in range(1, 9)])
ghosts[0].load_textures([f"../asset/ghost/{i}.png" for i in range(4, 5)])
ghosts[1].load_textures([f"../asset/ghost/{i}.png" for i in range(3, 4)])
ghosts[2].load_textures([f"../asset/ghost/{i}.png" for i in range(1, 2)])
ghosts[3].load_textures([f"../asset/ghost/{i}.png" for i in range(2, 3)])

while running:
    pacman.delay += 1
    ghosts[0].delay += 1
    ghosts[1].delay += 1
    ghosts[3].delay += 1

    for i in range(0, 4):
        ghosts_pos[i] = ghosts[i].pos
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pacman.last_request = 0
            elif event.key == pygame.K_s:
                pacman.last_request = 1
            elif event.key == pygame.K_a:
                pacman.last_request = 2
            elif event.key == pygame.K_d:
                pacman.last_request = 3
            else:
                pacman.last_request = -1

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # Draw map
    # maze.draw_grid(screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_W, BLOCK_H)
    maze.draw_map(screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_W, BLOCK_H)
    maze.draw_food(screen, BLOCK_W, BLOCK_H, food_pos)

    # Draw characters
    pacman.draw(screen, BLOCK_W, BLOCK_H)
    for i in range(0, 4):
        ghosts[i].draw(screen, BLOCK_W, BLOCK_H)
    
    # Update character's movement
    if pacman.delay == 2:
        pacman.move(maze, food_pos)
        pacman.delay = 0
    if ghosts[0].delay == 2:
        ghosts[0].move(maze, ghosts_pos, pacman.pos)
        ghosts[0].delay = 0
    if ghosts[1].delay == 2:
        ghosts[1].move(maze, ghosts_pos, pacman.pos)
        ghosts[1].delay = 0
    if ghosts[3].delay == 2:
        ghosts[3].move(maze, ghosts_pos, pacman.pos)
        ghosts[3].delay = 0

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)
pygame.quit()
