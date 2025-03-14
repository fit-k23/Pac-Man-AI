from search import *
from map import Map
from util import *
from defs import *
from collections import deque
import random

def bfs(mp, ghosts_pos, id, pacman_pos, succ_list):
    # Initialize queue, visited, and trace array
    queue = deque()
    visited = []
    trace = []
    start = [int(ghosts_pos[id][0]), int(ghosts_pos[id][1])]
    queue.append(start)

    for x in range(30):
        visited.append([False] * 33)
        trace.append([[-1, -1] for _ in range(33)])

    visited[int(start[0])][int(start[1])] = True
    
    found = False
    cnt_loop = 0
    while len(queue) > 0 and found == False:
        cur_pos = queue.popleft()

        if cur_pos == pacman_pos:
            found = True
            break
        
        for i in range(4):
            new_pos = [cur_pos[0] + dx[i], cur_pos[1] + dy[i]]

            if can_go(new_pos, mp) == False or visited[new_pos[0]][new_pos[1]] or (cur_pos == start and in_succ_list(succ_list, id, new_pos)):
                continue

            queue.append((new_pos))
            visited[int(new_pos[0])][int(new_pos[1])] = True
            trace[int(new_pos[0])][int(new_pos[1])] = cur_pos

            if new_pos == pacman_pos:
                found = True
                break

        cnt_loop += 1
        if cnt_loop >= 600:
            print("bfs wrong")
            break

    if not found:
        return [start]
    
    # Trace back to find path
    succ = []
    temp = [int(pacman_pos[0]), int(pacman_pos[1])]
    path = []
    while temp != ghosts_pos[id]:
        succ = temp
        path.append(succ)
        new_temp = trace[temp[0]][temp[1]]
        temp = new_temp

    path.reverse()

    del queue
    del trace

    if path == []:
        path = [start]

    return path