from queue import PriorityQueue
from util import *
from defs import *

def astar(mp, ghosts_pos, id, pacman_pos):
    pq = PriorityQueue()  
    dist = []
    trace = [] # trace[x][y] = [pre_x, pre_y]
    for i in range(30):
        col = []
        trace_arr = []
        for j in range(33):
            col.append(INF)
            trace_arr.append([-1, -1])
        dist.append(col)
        trace.append(trace_arr)
        
    init = (get_heuristic(ghosts_pos[id], pacman_pos), 0, [int(ghosts_pos[id][0]), int(ghosts_pos[id][1])]) 
    pq.put(init)
    dist[int(ghosts_pos[id][0])][int(ghosts_pos[id][1])] = get_heuristic(ghosts_pos[id], pacman_pos)
    while pq: 
        cur = pq.get()
        # print("cur = ", cur)
        if cur[2] == pacman_pos:
            break
        
        if cur[0] != dist[cur[2][0]][cur[2][1]]:
            continue
        
        for i in range(4):
            new_pos = [cur[2][0] + dx[i], cur[2][1] + dy[i]]
            if can_go(new_pos, mp) == False:
                continue
        
            h = get_heuristic(new_pos, pacman_pos)
            new_dist = cur[1] + 1
            
            if new_dist + h < dist[new_pos[0]][new_pos[1]]:
                pq.put((h + new_dist, new_dist, new_pos))
                dist[new_pos[0]][new_pos[1]] = new_dist + h
                trace[new_pos[0]][new_pos[1]] = cur[2]
        
    succ = []
    temp = [int(pacman_pos[0]), int(pacman_pos[1])]
    while temp != ghosts_pos[id]:
        succ = temp
        new_temp = trace[temp[0]][temp[1]]
        temp = new_temp

    occupied = False
    for i in range(0, 4): 
        if ghosts_pos[i] == succ:
            occupied = True

    if occupied:
        for i in range(0, 4):
            new_pos = [ghosts_pos[id][0] + dx[i], ghosts_pos[id][1] + dy[i]]
            if can_go(new_pos, mp) and new_pos != succ:
                return new_pos
        return ghosts_pos[id]
    return succ
                
        
                
                
            
            
                
                
            
            
            
            
            
            
            
    return None
