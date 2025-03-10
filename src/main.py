import pygame
from map import *
from pacman import *
from ghost import *
from algo import *



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

# ghost
dl = 0
director = 0

ghost_images = []
ghost_X = 450
ghost_Y = 663
collision_wall = [False, False, False, False]

# ghost_images.append(pygame.transform.scale(pygame.image.load(f'../pic/1.png'), (60, 60)))

# Map object
maze = Map.parse("../asset/maps/map_02.txt")

# Get position of pacman, ghosts, and food at first
(pacman_pos, ghosts_pos) = maze.get_character_pos()
food_pos = maze.get_food_pos() 
pacman = Pacman(pacman_pos)
pink_ghost = Pinky(ghosts_pos[1])
blue_ghost = Inky(ghosts_pos[2])
yellow_ghost = Clyde(ghosts_pos[0])
red_ghost = Blinky(ghosts_pos[3])

search = SearchProblem(pink_ghost, pacman, maze)

print(search.getStartState())
print(pacman.pos)
print("++++++")


solution = bfs(search)
for pos in solution:
    print(pos)


pacman.load_textures([f"../asset/pacman/pacman_{i}.png" for i in range(1, 9)])

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
    # maze.draw_grid(screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_W, BLOCK_H)
    maze.draw_map(screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_W, BLOCK_H)
    maze.draw_food(screen, BLOCK_W, BLOCK_H, food_pos)

    # Draw pacman
    pacman.draw(screen, BLOCK_W, BLOCK_H)
    pink_ghost.draw(screen, BLOCK_W, BLOCK_H)
    red_ghost.draw(screen, BLOCK_W, BLOCK_H)
    yellow_ghost.draw(screen, BLOCK_W, BLOCK_H)
    blue_ghost.draw(screen, BLOCK_W, BLOCK_H)
    

    # slow movement
    if pacman.delay == 2:
        pacman.move(maze, food_pos)
        pacman.delay = 0

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)
pygame.quit()
