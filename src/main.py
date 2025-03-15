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
maze = Map.parse(get_file_absolute_path("../asset/maps/map_02.txt"))

# Get position of pacman, ghosts, and food at first
(pacman_pos, ghosts_pos) = maze.get_character_pos()
food_pos = maze.get_food_pos() 
pacman = Pacman(pacman_pos)
ghosts = [Clyde(ghosts_pos[0], CLYDE, CLYDE_ALGO), Pinky(ghosts_pos[1], PINKY, PINKY_ALGO), Inky(ghosts_pos[2], INKY, INKY_ALGO),
          Blinky(ghosts_pos[3], BLINKY, BLINKY_ALGO)]

succ_list = []
for i in range(4):
    succ_list.append(ghosts_pos[i])

# Load character's textures
pacman.load_textures([get_file_absolute_path(f"../asset/pacman/pacman_{i}.png") for i in range(1, 9)])
ghosts[0].load_textures([get_file_absolute_path("../asset/ghost/4.png")])
ghosts[1].load_textures([get_file_absolute_path("../asset/ghost/3.png")])
ghosts[2].load_textures([get_file_absolute_path("../asset/ghost/1.png")])
ghosts[3].load_textures([get_file_absolute_path("../asset/ghost/2.png")])

# Text
last_score = -1
font_path = os.path.abspath(get_file_absolute_path("../asset/font/8-BIT WONDER.TTF"))
small_font = pygame.font.Font(font_path, 35)
big_font = pygame.font.Font(font_path, 60)

Sys_font = pygame.font.SysFont(None, 35)
score_text = small_font.render('Score: ' + str(pacman.score), False, WHITE)
score_pos1 = (32 * BLOCK_W - 3, 6 * BLOCK_H)
score_pos2 = (32 * BLOCK_W - 8, 6 * BLOCK_H + 5)

text = Sys_font.render('Quit' , True , "white")

# Drawing stuff on screen
def display_game():
    # Draw map
    # maze.draw_grid(screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_W, BLOCK_H)
    maze.draw_map(screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_W, BLOCK_H)

    # Draw map border
    pygame.draw.rect(screen, PURPLE, pygame.Rect(0, 0, 30 * BLOCK_W + 2, 32 * BLOCK_H + 20), 2, 8)
    
    mp = pygame.image.load(get_file_absolute_path(f"../asset/background/mini_pacman.png"))
    sb = pygame.image.load(get_file_absolute_path(f"../asset/background/board_game.png"))
    bb = pygame.image.load(get_file_absolute_path(f"../asset/background/board_game2.png"))
    
    sb = pygame.transform.scale(sb, (230, 39.2))
    mp = pygame.transform.scale(mp, (180, 27.1))
    bb = pygame.transform.scale(bb, (10 * BLOCK_W - 8, 440))
    
    screen.blit(sb, (30 * BLOCK_W + 7, 30))
    screen.blit(mp, (30 * BLOCK_W + 32, 70))

   
    pygame.draw.rect(screen, PURPLE, pygame.Rect(30 * BLOCK_W + 5, 0, 10 * BLOCK_W - 8, 10 * BLOCK_H + 20), 2, border_radius = 8)
    screen.blit(bb, (30 * BLOCK_W + 5, 12 * BLOCK_H - 8))
    
    # Draw characters
    for i in range(0, 4):
        ghosts[i].draw(screen, BLOCK_W, BLOCK_H)
    pacman.draw(screen, BLOCK_W, BLOCK_H)

    # Draw score    
    score_text1 = big_font.render(str(pacman.score).zfill(3), True, WHITE)
    score_text2 = big_font.render(str(pacman.score).zfill(3), True, BLUE_LIGHT)
    
    screen.blit(score_text2, score_pos2)
    screen.blit(score_text1, score_pos1)
    
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
            pygame.draw.rect(screen, BLUE_LIGHT, rect, border_radius = 20)
            pygame.draw.rect(screen, color_dark, rect, 3, 20)
        else:
            rect = pygame.Rect(button_x, button_y, BUTTON_W, BUTTON_H)
            pygame.draw.rect(screen, RASPBERRY_PINK, rect, border_radius = 20)
            pygame.draw.rect(screen, color_dark, rect, 3, 20)
        
        screen.blit(text, (BLOCK_W * (GRID_W / 2 - 1.1), BLOCK_H * (GRID_H / 2 + 10.7)))
    
    
        #Write score
        score_text = Sys_font.render('Score: ' + str(pacman.score), False, YELLOW)
        screen.blit(score_text, ((button_x + 2 * BLOCK_W), (BLOCK_H * 2)))
        
        # draw pacman
        image = pacman.textures[pacman.get_texture_index()]
        pacman.update_animation()
        image = pygame.transform.scale(image, (40, 40))
        screen.blit(image, (button_x, (BLOCK_H * 1.5)))
        
        pygame.display.flip()
        clock.tick(100)   

def show_start_menu():
    menu_image = pygame.image.load(get_file_absolute_path(f"../asset/background/game_start.png"))
    menu_image = pygame.transform.scale(menu_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2+75, 200, 60)
    button_text = font.render("Start", True, WHITE)
    button_rect2 = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 150, 200, 60)
    button_text2 = font.render("Quit", True, WHITE)

    running = True
    while running:
        mouse = pygame.mouse.get_pos()
        screen.blit(menu_image, (0, 0))
        if button_rect.x <= mouse[0] <= button_rect.x + 200 and button_rect.y <= mouse[1] <= button_rect.y+60:
            pygame.draw.rect(screen, BLUE_LIGHT, button_rect, border_radius=10)
            pygame.draw.rect(screen, color_dark, button_rect, 3, 10)
            screen.blit(button_text, (button_rect.x + 70, button_rect.y + 15))
        else:
            pygame.draw.rect(screen, RASPBERRY_PINK, button_rect, border_radius=10)
            pygame.draw.rect(screen, color_dark, button_rect, 3, 10)
            screen.blit(button_text, (button_rect.x + 70, button_rect.y + 15))
        if button_rect2.x <= mouse[0] <= button_rect2.x + 200 and button_rect2.y <= mouse[1] <= button_rect2.y+60:
            pygame.draw.rect(screen, BLUE_LIGHT, button_rect2, border_radius=10)
            pygame.draw.rect(screen, color_dark, button_rect, 3, 10)
            screen.blit(button_text2, (button_rect2.x + 72, button_rect2.y + 15))
        else:
            pygame.draw.rect(screen, RASPBERRY_PINK, button_rect2, border_radius=10)
            pygame.draw.rect(screen, color_dark, button_rect2, 3, 10)
            screen.blit(button_text2, (button_rect2.x + 72, button_rect2.y + 15))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(1)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect2.collidepoint(event.pos):
                    pygame.quit()
                    exit()
                if button_rect.collidepoint(event.pos):
                    running = False 

def update_delay():
    pacman.delay += 1
    ghosts[0].delay += 1
    ghosts[1].delay += 1
    ghosts[2].delay += 1
    ghosts[3].delay += 1

# Update after delay time for smoother movement
def update_character():
    delay_to_update = 2
    if pacman.delay == delay_to_update:
        pacman.move(maze, food_pos)
        pacman.delay = 0
    for i in range(4):
        if ghosts[i].delay == delay_to_update:
            # print("Turn", i, "cur pos", ghosts[i].pos, "limit", ghosts[i].algo_upd_limit)
            ghosts[i].move(maze, ghosts_pos, succ_list, pacman.pos)
            ghosts[i].delay = 0
            succ_list[i] = ghosts[i].successor
            # print("Ghost", i, "pos", ghosts[i].pos, "cnt", ghosts[i].algo_upd_cnt, "\npath", ghosts[i].algo_path)
            # print("Next successor is ", succ_list[i])
        
font_size = 36
font = pygame.font.Font(None, font_size)
show_start_menu()
while running:
    # Update delay for character's update
    update_delay()

    # Maintaining ghost positions into array ghosts_pos[]
    for i in range(0, 4):
        ghosts_pos[i] = ghosts[i].pos

    for i in range(4):
        for j in range(i + 1, 4):
            if ghosts_pos[i] == ghosts_pos[j]:
                print(i, j, ghosts_pos[i], succ_list[i], ghosts_pos[j], succ_list[j])

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

    fps = int(clock.get_fps())  # Convert to integer for clean display

    # Render FPS text
    fps_text = font.render(f"FPS: {fps}", True, (255, 255, 255))  # White color
    screen.blit(fps_text, (SCREEN_WIDTH - 100, SCREEN_HEIGHT - font_size))

    # Check if pacman is eaten by ghosts
    if Ghost.eat_pacman(ghosts_pos, pacman.pos) or not food_pos:
        running = False
        display_final_game()
        break

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()

    

