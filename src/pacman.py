from map import *

# Direction: 0 - up, 1 - down, 2 - left, 3 - right
class Pacman:
    pos = [0, 0]  # position on map (not real position on window)
    dir = 0  # current direction
    delay = 0  # delay for slow movement
    last_request = -1  # save the last request to change direction
    veloc = 1 / 4  # velocity of pacman

    # Constructor
    def __init__(self, _pos):
        self.pos = _pos
        self.dir = 0
        self.last_request = -1
        self.veloc = 1 / 4

        self.textures = []
        self.__texture_index = -1
        self.__last_update = pygame.time.get_ticks()
        self.__animation_speed = 50 # 50ms

    def load_textures(self, texture_list):
        print(texture_list)
        for texture in texture_list:
            print(texture)
            image = pygame.image.load(texture)
            self.textures.append(pygame.transform.scale(image, (32, 32)))
            self.__texture_index = 0

    def update_animation(self):
        now = pygame.time.get_ticks()
        if now - self.__last_update > self.__animation_speed:
            self.__last_update = now
            self.__texture_index = (self.__texture_index + 1) % len(self.textures)

    # Check if a block can be reached by characters
    def can_go(self, check_pos, mp) -> bool:
        # TODO: update teleport if out of map
        if int(check_pos[0]) < 0 or int(check_pos[0]) >= 30 or int(check_pos[1]) < 0 or int(check_pos[1]) >= 33:
            return False
        if '3' <= mp.data[int(check_pos[1])][int(check_pos[0])] <= '8':
            return False
        return True

    # Update direction according to last request
    def update_dir(self):
        self.dir = self.last_request
        self.last_request = -1

    # Check if pacman can teleport through map
    def teleport(self, mp, d, is_upd):
        if d == 0:
            if self.pos[0] % 1.0 == 0 and self.pos[1] == 0:
                if self.can_go([self.pos[0], 32], mp):
                    self.pos[1] = 32
                    if is_upd:
                        self.update_dir()
                    return True
        elif d == 1:
            if self.pos[0] % 1.0 == 0 and self.pos[1] == 32:
                if self.can_go([self.pos[0], 0], mp):
                    self.pos[1] = 0
                    if is_upd:
                        self.update_dir()
                    return True
        elif d == 2:
            if self.pos[1] % 1.0 == 0 and self.pos[0] == 0:
                if self.can_go([29, self.pos[1]], mp):
                    self.pos[0] = 29
                    if is_upd:
                        self.update_dir()
                    return True
        elif d == 3:
            if self.pos[1] % 1.0 == 0 and self.pos[0] == 29:
                if self.can_go([0, self.pos[1]], mp):
                    self.pos[0] = 0
                    if is_upd:
                        self.update_dir()
                    return True
        return False

    # Move the pacman along blocks
    def move(self, mp, food_pos):
        offset_check_turn = 0.9
        # If there are keyboard pressed (W, S, A, D)
        if self.last_request != -1:
            # Check if pacman can teleport
            if self.teleport(mp, self.last_request, True):
                return
            match self.last_request:
                case 0:
                    if self.can_go([self.pos[0], math.floor(self.pos[1] - self.veloc)], mp) and self.pos[0] % 1.0 == 0:
                        self.pos[1] -= self.veloc
                        self.update_dir()
                        return
                case 1:
                    if self.can_go([self.pos[0], math.floor(self.pos[1] + offset_check_turn + self.veloc)], mp) and self.pos[0] % 1.0 == 0:
                        self.pos[1] += self.veloc
                        self.update_dir()
                        return
                case 2:
                    if self.can_go([math.floor(self.pos[0] - self.veloc), self.pos[1]], mp) and self.pos[1] % 1.0 == 0:
                        self.pos[0] -= self.veloc
                        self.update_dir()
                        return
                case 3:
                    if self.can_go([math.floor(self.pos[0] + offset_check_turn + self.veloc), self.pos[1]], mp) and self.pos[1] % 1.0 == 0:
                        self.pos[0] += self.veloc
                        self.update_dir()
                        return

        # If the code can reach here, then there are either no requests or the last request can't be performed.
        # So we keep moving current direction (if possible).

        # Check if pacman can teleport
        if self.teleport(mp, self.dir, False):
            return

        match self.dir:
            case 0:
                if self.can_go([self.pos[0], math.floor(self.pos[1] - self.veloc)], mp) and self.pos[0] % 1.0 == 0:
                    self.pos[1] -= self.veloc
            case 1:
                if self.can_go([self.pos[0], math.floor(self.pos[1] + offset_check_turn + self.veloc)], mp) and self.pos[0] % 1.0 == 0:
                    self.pos[1] += self.veloc
            case 2:
                if self.can_go([math.floor(self.pos[0] - self.veloc), self.pos[1]], mp) and self.pos[1] % 1.0 == 0:
                    self.pos[0] -= self.veloc
            case 3:
                if self.can_go([math.floor(self.pos[0] + offset_check_turn + self.veloc), self.pos[1]], mp) and self.pos[1] % 1.0 == 0:
                    self.pos[0] += self.veloc
                    
        mp.delete_food(food_pos, self.pos[1], self.pos[0])

    # Draw pacman
    def draw(self, screen, block_width, block_height):
        if self.__texture_index == -1:
            return
        self.update_animation()
        image = self.textures[self.__texture_index]
        if self.dir == 0:
            image = pygame.transform.rotate(image, 90)
        elif self.dir == 1:
            image = pygame.transform.rotate(image, -90)
        elif self.dir == 2:
            image = pygame.transform.flip(image, True, False)  # Flip horizontally

        screen.blit(image, ((self.pos[0] - 0.25) * block_width, (self.pos[1] - 0.25) * block_height))
