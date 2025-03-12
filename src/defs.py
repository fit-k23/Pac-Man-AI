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

# Screen, Block parameters
SCREEN_WIDTH: int = 750
SCREEN_HEIGHT: int = 660
BLOCK_W: int = SCREEN_WIDTH // 30
BLOCK_H: int = SCREEN_HEIGHT // 33

# GHOST_ID
CLYDE = 0 # yellow ghost -> UCS-2
PINKY = 1 # pink ghost -> DFS-1
INKY = 2 # blue ghost -> BFS-0
BLINKY = 3 # red ghost -> A*-3

# ALGO_ID
PINKY_ALGO = 1
INKY_ALGO = 0
CLYDE_ALGO = 2
BLINKY_ALGO = 3

# Infinity value
INF = 99999

# up, down, left, right
# 0 1 2 3
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]