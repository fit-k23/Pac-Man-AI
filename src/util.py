import sys
import random


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
    

    

    


