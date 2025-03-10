from enum import Enum
from character import *
from pacman import *
import util

class GhostState(Enum):
    IDLE = 0 # Doing absolutely nothing
    REST = 1 # Resting in the cage, moving up and down
    WONDER = 2 # Move around randomly, doing random stuff
    TARGETED = 3 # Rush toward pacman, targeted hunting
    RUN_AWAY = 4 # Run away from pacman

class Ghost(Characters):
    def __init__(self, _pos):
        super().__init__(_pos)  # Gọi constructor của Characters
        self.state = GhostState.IDLE
        
            
         

class Pinky(Ghost):
    def __init__(self, _pos):
        super().__init__(_pos)  # Gọi constructor của Ghost
        self.load_textures(["../asset/ghost/3.png"])  # Tải sprite
        
        
        
class Blinky(Ghost):
    def __init__(seft, _pos):
        super().__init__(_pos)
        seft.load_textures(["../asset/ghost/2.png"])
        
class Inky(Ghost):
    def __init__(seft, _pos):
        super().__init__(_pos)
        seft.load_textures(["../asset/ghost/1.png"])
        
class Clyde(Ghost):
    def __init__(seft, _pos):
        super().__init__(_pos)
        seft.load_textures(["../asset/ghost/4.png"])
        
    
