from search import *
from map import Map
from util import *
from defs import *
import queue
import random

def bfs(mp, ghosts_pos, id, pacman_pos, forbid = []):
    # Initialize queue, visited, and trace array
    queue = []
    visited = []
    trace = []
    start = [int(ghosts_pos[id][0]), int(ghosts_pos[id][1])]
    queue.append(start)

    for x in range(30):
        visited.append([False] * 33)
        trace.append([[-1, -1] for _ in range(33)])

    visited[int(start[0])][int(start[1])] = True
    if forbid != []:
        visited[int(forbid[0])][int(forbid[1])] = True
        print("bfs ", forbid)

    found = False
    while len(queue) > 0 and found == False:
        cur_pos = queue.pop(0)

        if cur_pos == pacman_pos:
            break

        rdom_succ = [0, 1, 2, 3]
        # If there is a forbidden position, choose successor randomly to avoid cycle
        if forbid != [] and cur_pos == start:
            random.shuffle(rdom_succ)
        
        for i in range(4):
            new_pos = [cur_pos[0] + dx[rdom_succ[i]], cur_pos[1] + dy[rdom_succ[i]]]

            if can_go(new_pos, mp) and not visited[int(new_pos[0])][int(new_pos[1])]:
                queue.append((new_pos))
                visited[int(new_pos[0])][int(new_pos[1])] = True
                trace[int(new_pos[0])][int(new_pos[1])] = cur_pos

                if new_pos == pacman_pos:
                    found = True
                    break

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

    del queue[:]
    del trace[:]

    return path