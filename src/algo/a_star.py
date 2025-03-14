from queue import PriorityQueue
from util import *
from defs import *

def astar(mp, ghosts_pos, id, pacman_pos, succ_list):
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
    
    start = [int(ghosts_pos[id][0]), int(ghosts_pos[id][1])]

    init = (get_heuristic(ghosts_pos[id], pacman_pos), 0, start) 
    pq.put(init)
    dist[int(ghosts_pos[id][0])][int(ghosts_pos[id][1])] = get_heuristic(ghosts_pos[id], pacman_pos)

    # if forbid:
    #     print("A* ", forbid)

    found = False
    while pq.qsize() > 0: 
        cur = pq.get()
        # print("cur = ", cur)
        if cur[2] == pacman_pos:
            found = True
            break
        
        if cur[0] != dist[cur[2][0]][cur[2][1]]:
            continue
        
        for i in range(4):
            new_pos = [cur[2][0] + dx[i], cur[2][1] + dy[i]]

            if can_go(new_pos, mp) == False:
                continue

            if cur[2] == start and in_succ_list(succ_list, id, new_pos):
                # print("A* will find diff path")
                continue
        
            h = get_heuristic(new_pos, pacman_pos)
            new_dist = cur[1] + 1
            
            if new_dist + h < dist[new_pos[0]][new_pos[1]]:
                pq.put((h + new_dist, new_dist, new_pos))
                dist[new_pos[0]][new_pos[1]] = new_dist + h
                trace[new_pos[0]][new_pos[1]] = cur[2]
    
    if not found:
        # print("A* cannot found destination")
        return [start]
        
    # Trace back to find optimal successor
    succ = []
    temp = [int(pacman_pos[0]), int(pacman_pos[1])]
    path = []
    while temp != ghosts_pos[id]:
        succ = temp
        path.append(succ)
        new_temp = trace[temp[0]][temp[1]]
        temp = new_temp
    
    path.reverse()
    
    del pq
    del dist
    del trace
    
    if path == []:
        path = [start]

    return path