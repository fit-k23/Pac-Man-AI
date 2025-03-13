import pygame
from map import *
from pacman import *
from ghost import *
from algo import *
from defs import *

# pygame setup
pygame.init()
pygame.font.init()
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

# Text
last_score = -1
score_font = pygame.font.SysFont('Times New Roman', 30)
score_text = score_font.render('Score: ' + str(pacman.score), False, WHITE)
score_pos = (32 * BLOCK_W, 5 * BLOCK_H)

# Drawing stuff on screen
def display_game():
    # Draw map
    # maze.draw_grid(screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_W, BLOCK_H)
    maze.draw_map(screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_W, BLOCK_H)
    maze.draw_food(screen, BLOCK_W, BLOCK_H, food_pos)

    # Draw map border
    pygame.draw.rect(screen, PURPLE, pygame.Rect(0, 0, 30 * BLOCK_W + 2, 32 * BLOCK_H + 20), 2)

    # Draw characters
    pacman.draw(screen, BLOCK_W, BLOCK_H)
    for i in range(0, 4):
        ghosts[i].draw(screen, BLOCK_W, BLOCK_H)

    # Draw text
    global last_score
    global score_text
    if pacman.score != last_score:
        score_text = score_font.render('Score: ' + str(pacman.score), False, WHITE)
        last_score = pacman.score
    screen.blit(score_text, score_pos)

def update_delay():
    pacman.delay += 1
    ghosts[0].delay += 1
    ghosts[1].delay += 1
    ghosts[3].delay += 1

# Update after delay time for smoother movement
def update_character():
    delay_to_update = 3
    if pacman.delay == delay_to_update:
        pacman.move(maze, food_pos)
        pacman.delay = 0
    if ghosts[0].delay == delay_to_update:
        ghosts[0].move(maze, ghosts_pos, pacman.pos)
        ghosts[0].delay = 0
    if ghosts[1].delay == delay_to_update:
        ghosts[1].move(maze, ghosts_pos, pacman.pos)
        ghosts[1].delay = 0
    if ghosts[3].delay == delay_to_update:
        ghosts[3].move(maze, ghosts_pos, pacman.pos)
        ghosts[3].delay = 0

while running:
    # Update delay for character's update
    update_delay()

    # Maintaining ghost positions into array ghosts_pos[]
    for i in range(0, 4):
        ghosts_pos[i] = ghosts[i].pos

    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                pacman.last_request = 0
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                pacman.last_request = 1
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                pacman.last_request = 2
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                pacman.last_request = 3
            else:
                pacman.last_request = -1

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # Draw game onto screen
    display_game()
    
    # Update character's movement
    update_character()

    # Check if pacman is eaten by ghosts
    if Ghost.eat_pacman(ghosts_pos, pacman.pos):
        running = False

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(100)
pygame.quit()
