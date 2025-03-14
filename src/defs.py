# COLOR
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
PURPLE = (255, 0, 255)
color_light = (227,80,168)  
color_dark = (149,67,167)
blue_dark = (106,156,253)
blue_light = (0,255,255)

# Screen, Block parameters
GRID_W: int = 40
GRID_H: int = 33
BLOCK_W: int = 25 
BLOCK_H: int = 20 
SCREEN_WIDTH: int = GRID_W * BLOCK_W
SCREEN_HEIGHT: int = GRID_H * BLOCK_H

# GHOST_ID
CLYDE = 0 # yellow ghost -> UCS-2
PINKY = 1 # pink ghost -> DFS-1
INKY = 2 # blue ghost -> BFS-0
BLINKY = 3 # red ghost -> A*-3

# ALGO_ID
PINKY_ALGO = 1 # DFS
INKY_ALGO = 0 # BFS
CLYDE_ALGO = 2 # UCS
BLINKY_ALGO = 3 # A*

# Infinity value
INF = 99999

# up, down, left, right
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# button
BUTTON_W = BLOCK_W * 5
BUTTON_H = BLOCK_H * 2.5
button_x = BLOCK_W * (GRID_W / 2 - 2.5)
button_y = BLOCK_H * (GRID_H / 2 + 10)

