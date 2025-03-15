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
font_path = os.path.abspath(get_file_absolute_path("../asset/font/8-BIT WONDER.TTF"))
small_font = pygame.font.Font(font_path, 35)
big_font = pygame.font.Font(font_path, 60)
sys_font = pygame.font.SysFont(None, 35)
score_pos1 = (32 * BLOCK_W - 3, 6 * BLOCK_H)
score_pos2 = (32 * BLOCK_W - 8, 6 * BLOCK_H + 5)
button_text2 = sys_font.render("Quit", True, WHITE)
text = sys_font.render('Quit' , True , "white")
button_text = sys_font.render("Start", True, WHITE)
font_size = 36


# Button
button_rect3 = pygame.Rect(button_x, button_y, BUTTON_W, BUTTON_H)
button_rect = pygame.Rect(button_x, SCREEN_HEIGHT // 2+75, BUTTON_W, BUTTON_H)
button_rect2 = pygame.Rect(button_x, SCREEN_HEIGHT // 2 + 150, BUTTON_W, BUTTON_H)

class GameState:
    def handle_event(self, game_manage):
        pass

    def update(self, game_manage):
        pass

    def draw(self, screen):
        pass

class EndScreen(GameState):
    def handle_event(self, game_manage):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                game_manage.running = False
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if button_rect3.collidepoint(ev.pos):
                  game_manage.running = False

    def draw(self, _screen):
        bg = pygame.image.load(get_file_absolute_path("../asset/background/game_over.png"))
        _screen.blit(bg, (0, 0))


        #Write score
        score_text = sys_font.render('Score: ' + str(pacman.score), False, YELLOW)
        _screen.blit(score_text, ((button_x + 2 * BLOCK_W), (BLOCK_H * 2)))

        # draw pacman
        image = pacman.textures[pacman.get_texture_index()]
        pacman.update_animation()
        image = pygame.transform.scale(image, (40, 40))
        _screen.blit(image, (button_x, (BLOCK_H * 1.5)))

        mouse = pygame.mouse.get_pos()

        if button_x <= mouse[0] <= button_x + BUTTON_W and button_y <= mouse[1] <= button_y + BUTTON_H:
            pygame.draw.rect(_screen, BLUE_LIGHT, button_rect3, border_radius = 20)
            pygame.draw.rect(_screen, color_dark, button_rect3, 3, 20)
        else:
            pygame.draw.rect(_screen, RASPBERRY_PINK, button_rect3, border_radius = 20)
            pygame.draw.rect(_screen, color_dark, button_rect3, 3, 20)

        _screen.blit(text, (BLOCK_W * (GRID_W / 2 - 1.1), BLOCK_H * (GRID_H / 2 + 10.7)))


menu_image = pygame.image.load(get_file_absolute_path("../asset/background/game_start.png"))
menu_image = pygame.transform.scale(menu_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

def mouse_over_button(_button_rect, _mouse_pos) -> bool:
    return _button_rect.x <= _mouse_pos[0] <= _button_rect.x + 200 and _button_rect.y <= _mouse_pos[1] <= _button_rect.y + 60

class StartScreen(GameState):
    def __init__(self):
        pygame.mixer.music.load(get_file_absolute_path("../asset/music/pacman_ost.mp3"))
        pygame.mixer.music.play()

    def handle_event(self, game_manage):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect2.collidepoint(event.pos):
                    pygame.quit()
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    pygame.mixer.music.fadeout(500)
                    game_manage.change_state(GameScreen())

    def draw(self, _screen):
        mouse = pygame.mouse.get_pos()
        _screen.blit(menu_image, (0, 0))
        pygame.draw.rect(_screen, BLUE_LIGHT if mouse_over_button(button_rect, mouse) else RASPBERRY_PINK, button_rect, border_radius=10)
        pygame.draw.rect(_screen, color_dark, button_rect, 3, 10)
        _screen.blit(button_text, (BLOCK_W * (GRID_W / 2 - 1.1), button_rect.y + 15))

        pygame.draw.rect(_screen, BLUE_LIGHT if mouse_over_button(button_rect2, mouse) else RASPBERRY_PINK, button_rect2, border_radius=10)
        pygame.draw.rect(_screen, color_dark, button_rect2, 3, 10)
        _screen.blit(button_text2, (BLOCK_W * (GRID_W / 2 - 1.1), button_rect2.y + 15))

        pygame.display.update()


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


class GameScreen(GameState):
    def handle_event(self, game_manage):
            # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_w | pygame.K_UP:
                        pacman.last_request = 0
                    case pygame.K_s | pygame.K_DOWN:
                        pacman.last_request = 1
                    case pygame.K_a | pygame.K_LEFT:
                        pacman.last_request = 2
                    case pygame.K_d | pygame.K_RIGHT:
                        pacman.last_request = 3
                    case _:
                        pacman.last_request = -1

        if Ghost.eat_pacman(ghosts_pos, pacman.pos) or not food_pos:
            game_manage.change_state(EndScreen())

    def update(self, game_manage):
        # Update delay for character's update
        update_delay()

        # Maintaining ghost positions into array ghosts_pos[]
        for i in range(0, 4):
            ghosts_pos[i] = ghosts[i].pos

        update_character()

    def draw(self, _screen):
        _screen.fill("black")
        # maze.draw_grid(screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_W, BLOCK_H)
        # Draw map
        maze.draw_map(_screen, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_W, BLOCK_H)
        # maze.draw_food(screen, BLOCK_W, BLOCK_H, food_pos)

        # Draw map border
        pygame.draw.rect(_screen, PURPLE, pygame.Rect(0, 0, 30 * BLOCK_W + 2, 32 * BLOCK_H + 20), 2, 8)

        mp = pygame.image.load(get_file_absolute_path("../asset/background/mini_pacman.png"))
        sb = pygame.image.load(get_file_absolute_path("../asset/background/board_game.png"))
        bb = pygame.image.load(get_file_absolute_path("../asset/background/board_game2.png"))

        sb = pygame.transform.scale(sb, (230, 39.2))
        mp = pygame.transform.scale(mp, (180, 27.1))
        bb = pygame.transform.scale(bb, (10 * BLOCK_W - 8, 440))

        _screen.blit(sb, (30 * BLOCK_W + 7, 30))
        _screen.blit(mp, (30 * BLOCK_W + 32, 70))


        pygame.draw.rect(_screen, PURPLE, pygame.Rect(30 * BLOCK_W + 5, 0, 10 * BLOCK_W - 8, 10 * BLOCK_H + 20), 2, border_radius = 8)
        _screen.blit(bb, (30 * BLOCK_W + 5, 12 * BLOCK_H - 8))

        # Draw characters
        score_text1 = big_font.render(str(pacman.score).zfill(3), False, WHITE)
        score_text2 = big_font.render(str(pacman.score).zfill(3), False, BLUE_LIGHT)

        _screen.blit(score_text2, score_pos2)
        _screen.blit(score_text1, score_pos1)

        pacman.draw(_screen, BLOCK_W, BLOCK_H)
        for i in range(0, 4):
            ghosts[i].draw(_screen, BLOCK_W, BLOCK_H)

        # Render FPS text
        fps = int(clock.get_fps())
        fps_text = sys_font.render(f"FPS: {fps}", True, (255, 255, 255))  # White color
        _screen.blit(fps_text, (SCREEN_WIDTH - 100, SCREEN_HEIGHT - font_size))


class GameManager():
    def __init__(self):
        self.current_state = StartScreen()
        self.running = True

    def change_state(self, new_state):
        self.current_state = new_state

    def run(self):
        while self.running:
            self.current_state.handle_event(self)
            self.current_state.update(self)
            self.current_state.draw(screen)
            pygame.display.flip()
            clock.tick(60)
