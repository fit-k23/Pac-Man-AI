import pygame
from map import *
from pacman import *

# Screen, Block paramters
BLOCK_W = 30
BLOCK_H = 23
SCREEN_WIDTH = BLOCK_W * 30
SCREEN_HEIGHT = BLOCK_H * 33

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True


# def check_position(centerx, centery):
#     turns = [False, False, False, False]
#     check_distance = 15 #the least possible distance from the person to the wall
#     if centerx // 30 < 29:
#         if director == 0:
#             if int(maze.data[centery // BLOCK_SIZE][(centerx + check_distance) // BLOCK_SIZE]) < 3:
#                 turns[0] = True
#         if director == 1:
#             if int(maze.data[centery // BLOCK_SIZE][(centerx - check_distance) // BLOCK_SIZE]) < 3:
#                 turns[1] = True
#         if director == 2:
#             if int(maze.data[centery - check_distance// BLOCK_SIZE][(centerx) // BLOCK_SIZE]) < 3:
#                 turns[2] = True   
#         if director == 3:
#             if int(maze.data[centery + check_distance // BLOCK_SIZE][(centerx + check_distance) // BLOCK_SIZE]) < 3:
#                 turns[3] = True
#         else:
#             turns[1] = False
#             turns[0] = False
#             turns[2] = False
#             turns[3] = False
#     return turns    

# ghost
dl = 0
director = 0

ghost_images = []
ghost_X = 450
ghost_Y = 663
collision_wall = [False, False, False, False]

ghost_images.append(pygame.transform.scale(pygame.image.load(f'../pic/1.png'), (60, 60)))
    
def draw_ghost():
    #RIGHT
    if director == 0:
        screen.blit(ghost_images[0], (ghost_X, ghost_Y))
    if director == 1:
    #LEFT
        screen.blit(pygame.transform.flip(ghost_images[0], True, False), (ghost_X, ghost_Y))
    if director == 2:
    #TOP
        screen.blit(pygame.transform.rotate(ghost_images[0], 90), (ghost_X, ghost_Y))
    #DOWN
    if director == 3:
        screen.blit(pygame.transform.rotate(ghost_images[0], 270), (ghost_X, ghost_Y))     

# Map object
maze = Map.parse("../asset/maps/map_02.txt") 

# Get position of pacman and ghosts at first
(pacman_pos, ghosts_pos) = maze.getCharacterPos()
pacman = PacMan(pacman_pos)

while running:
    pacman.delay += 1
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
    # maze.drawGrid(screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_W, BLOCK_H)
    maze.drawMap(screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_W, BLOCK_H)

    # Draw pacman
    pacman.draw(screen, BLOCK_W, BLOCK_H)
    # draw_ghost()
    
    # slow movement
    if pacman.delay == 10:
        pacman.move(maze.data)
        pacman.delay = 0

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]:
    #     director = 2
    #     ghost_Y -= 300 * dt
    # if keys[pygame.K_s]:
    #     director = 3
    #     ghost_Y += 300 * dt
    # if keys[pygame.K_d]:
    #     director = 0
    #     ghost_X += 300 * dt
    # if keys[pygame.K_a]:
    #     director = 1
    #     ghost_X -= 300 * dt
    
    # collision_wall = check_position(ghost_X, ghost_Y)
    
    # if director == 0 and collision_wall[0] == True:
    #     ghost_X += 300 * dt
    # if director == 1 and collision_wall[1] == True:
    #     ghost_X -= 300 * dt
    # if director == 2 and collision_wall[2] == True:
    #     ghost_Y -= 300 * dt
    # if director == 3 and collision_wall[3] == True:
    #     ghost_Y += 300 * dt

    # if ghost_X > 900:
    #     ghost_X = 0
    # if ghost_X < 0:
    #     ghost_X = 900
    # if ghost_Y > 990:
    #     ghost_Y = 0
    # if ghost_Y < 0:
    #     ghost_Y = 990
    # flip() the display to put your work on screen
    pygame.display.flip()

    # dt = clock.tick(60) / 1000 # limits FPS to 60
    clock.tick(90)
pygame.quit()
