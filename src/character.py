from map import*

class Characters:
    def __init__(self, pos=(0, 0), veloc=1/4):
        self.pos = pos  # Vị trí trên bản đồ (dùng list để có thể thay đổi)
        self.dir = -1  # Hướng di chuyển hiện tại
        self.delay = 0  # Độ trễ di chuyển
        self.last_request = -1  # Lần cuối yêu cầu đổi hướng
        self.veloc = veloc  # Vận tốc di chuyển
        self.textures = []
        # Thuộc tính riêng tư (private)
        self.__texture_index = -1
        self.__last_update = pygame.time.get_ticks()
        self.__animation_speed = 50  # 50ms mỗi frame animation
    
    
    # Update direction according to last request
    def update_dir(self):
        self.dir = self.last_request
        self.last_request = -1
        
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
    def move(self, mp):
        offset_check_turn = 0.9
        # If there are keyboard pressed (W, S, A, D)
        if self.last_request != -1:
            # Check if pacman can teleport
            if self.teleport(mp, self.last_request, True):
                return
            if self.last_request == 0:
                if self.can_go([self.pos[0], math.floor(self.pos[1] - self.veloc)], mp) and self.pos[0] % 1.0 == 0:
                    self.pos[1] -= self.veloc
                    self.update_dir()
                    return
            elif self.last_request == 1:
                if self.can_go([self.pos[0], math.floor(self.pos[1] + offset_check_turn + self.veloc)], mp) and self.pos[0] % 1.0 == 0:
                    self.pos[1] += self.veloc
                    self.update_dir()
                    return
            elif self.last_request == 2:
                if self.can_go([math.floor(self.pos[0] - self.veloc), self.pos[1]], mp) and self.pos[1] % 1.0 == 0:
                    self.pos[0] -= self.veloc
                    self.update_dir()
                    return
            elif self.last_request == 3:
                if self.can_go([math.floor(self.pos[0] + offset_check_turn + self.veloc), self.pos[1]], mp) and self.pos[1] % 1.0 == 0:
                    self.pos[0] += self.veloc
                    self.update_dir()
                    return

        # If the code can reach here, then there are either no requests or the last request can't be performed.
        # So we keep moving current direction (if possible).

        # Check if pacman can teleport
        if self.teleport(mp, self.dir, False):
            return

        if self.dir == 0:
            if self.can_go([self.pos[0], math.floor(self.pos[1] - self.veloc)], mp) and self.pos[0] % 1.0 == 0:
                self.pos[1] -= self.veloc
        elif self.dir == 1:
            if self.can_go([self.pos[0], math.floor(self.pos[1] + offset_check_turn + self.veloc)], mp) and self.pos[0] % 1.0 == 0:
                self.pos[1] += self.veloc
        elif self.dir == 2:
            if self.can_go([math.floor(self.pos[0] - self.veloc), self.pos[1]], mp) and self.pos[1] % 1.0 == 0:
                self.pos[0] -= self.veloc
        elif self.dir == 3:
            if self.can_go([math.floor(self.pos[0] + offset_check_turn + self.veloc), self.pos[1]], mp) and self.pos[1] % 1.0 == 0:
                self.pos[0] += self.veloc
            

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
            

