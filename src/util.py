import sys
import random

# Check if position is valid
# check_pos is array type [], (x, y) coordinates
def can_go(check_pos, mp) -> bool:
    if int(check_pos[0]) < 0 or int(check_pos[0]) >= 30 or int(check_pos[1]) < 0 or int(check_pos[1]) >= 33:
        return False
    if '3' <= mp.data[int(check_pos[1])][int(check_pos[0])] <= '8': # wall
        return False
    return True

# Chosen heuristic function is Manhattan
# Even though Manhattan and Euclidean distance are both consistent, Manhattan dominates Euclidean
def get_heuristic(pos, goal_pos):
    return abs(pos[0] - goal_pos[0]) + abs(pos[1] - goal_pos[1])

class stack:
    def __init__(self):
        self.list = []
        
    def push(self, value):
        self.list.append(value)
        
    def pop(self):
        return self.list.pop()
    
    def isEmpty(self):
        return len(self.list) == 0

class queue:
    def __init__(self):
        self.list = []
        
    def push(self, value):
        self.list.insert(0, value)
        
    def pop(self):
        return self.list.pop()
    
    def isEmpty(self):
        return len(self.list) == 0
    

    

    


