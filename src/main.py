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
game = True

import os
run_path = os.path.dirname(os.path.abspath(__file__))
def get_file_absolute_path(file_path):
    return os.path.abspath(str(os.path.join(run_path, file_path)))

# Map object
# maze = Map.parse("../asset/maps/map_02.txt")
maze = Map.parse(get_file_absolute_path("../asset/maps/map_02.txt"))

# Get position of pacman, ghosts, and food at first
(pacman_pos, ghosts_pos) = maze.get_character_pos()
food_pos = maze.get_food_pos() 
pacman = Pacman(pacman_pos)
ghosts = [Clyde(ghosts_pos[0], CLYDE, CLYDE_ALGO), Pinky(ghosts_pos[1], PINKY, PINKY_ALGO), Inky(ghosts_pos[2], INKY, INKY_ALGO),
          Blinky(ghosts_pos[3], BLINKY, BLINKY_ALGO)]

# Load character's textures
pacman.load_textures([get_file_absolute_path(f"../asset/pacman/pacman_{i}.png") for i in range(1, 9)])
ghosts[0].load_textures([get_file_absolute_path("../asset/ghost/4.png")])
ghosts[1].load_textures([get_file_absolute_path("../asset/ghost/3.png")])
ghosts[2].load_textures([get_file_absolute_path("../asset/ghost/1.png")])
ghosts[3].load_textures([get_file_absolute_path("../asset/ghost/2.png")])

# Text
last_score = -1
score_font = pygame.font.SysFont('Times New Roman', 30)
score_text = score_font.render('Score: ' + str(pacman.score), False, WHITE)
score_pos = (32 * BLOCK_W, 5 * BLOCK_H)
smallfont = pygame.font.SysFont('Corbel',35)
text = smallfont.render('Quit' , True , "white")

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
    # global last_score
    # global score_text
    # if pacman.score != last_score:
    #     score_text = score_font.render('Score: ' + str(pacman.score), False, WHITE)
    #     last_score = pacman.score
    # screen.blit(score_text, score_pos)
    
    
def display_final_game():
    running_final_game = True
    while running_final_game:
        bg = pygame.image.load(get_file_absolute_path(f"../asset/background/game_over.png"))
        #draw background
        screen.blit(bg, (0, 0))
    
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running_final_game = False
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                if button_x <= mouse[0] <= button_x + BUTTON_W and button_y <= mouse[1] <= button_y + BUTTON_H: 
                  running_final_game = False  
        
        mouse = pygame.mouse.get_pos()
        
        
        if button_x <= mouse[0] <= button_x + BUTTON_W and button_y <= mouse[1] <= button_y + BUTTON_H: 
            rect = pygame.Rect(button_x, button_y, BUTTON_W, BUTTON_H)
            pygame.draw.rect(screen, blue_dark, rect, border_radius=6)
            pygame.draw.rect(screen, color_dark, rect, 3, 6)
        else:
            rect = pygame.Rect(button_x, button_y, BUTTON_W, BUTTON_H)
            pygame.draw.rect(screen, color_light, rect, border_radius=6)
            pygame.draw.rect(screen, color_dark, rect, 3, 6)
        
        screen.blit(text, (BLOCK_W * (GRID_W / 2 - 1.1), BLOCK_H * (GRID_H / 2 + 10.7)))
    
    
        #Write score
        score_text = smallfont.render('Score: ' + str(pacman.score), False, YELLOW)
        screen.blit(score_text, ((button_x + 2 * BLOCK_W), (BLOCK_H * 2)))
        
        # draw pacman
        image = pacman.textures[pacman.get_texture_index()]
        pacman.update_animation()
        image = pygame.transform.scale(image, (40, 40))
        screen.blit(image, (button_x, (BLOCK_H * 1.5)))
    
        
        pygame.display.flip()
        clock.tick(100)    
    

def update_delay():
    pacman.delay += 1
    ghosts[0].delay += 1
    ghosts[1].delay += 1
    ghosts[2].delay += 1
    ghosts[3].delay += 1

# Update after delay time for smoother movement
def update_character():
    delay_to_update = 3
    if pacman.delay == delay_to_update:
        pacman.move(maze, food_pos)
        pacman.delay = 0
    for i in range(4):
        if ghosts[i].delay == delay_to_update:
            ghosts[i].move(maze, ghosts_pos, pacman.pos)
            ghosts[i].delay = 0

font_size = 36
font = pygame.font.Font(None, font_size)

while game:
    while running:
        # Update delay for character's update
        update_delay()

        # Maintaining ghost positions into array ghosts_pos[]
        for i in range(0, 4):
            ghosts_pos[i] = ghosts[i].pos

        # poll for events
        # print(pygame.event.get())
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

        fps = int(clock.get_fps())  # Convert to integer for clean display

        # Render FPS text
        fps_text = font.render(f"FPS: {fps}", True, (255, 255, 255))  # White color
        screen.blit(fps_text, (SCREEN_WIDTH - 100, SCREEN_HEIGHT - font_size))

        # Check if pacman is eaten by ghosts
        if Ghost.eat_pacman(ghosts_pos, pacman.pos):
            running = False

        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(100)
    
    display_final_game()
    
    break
pygame.quit()

    

