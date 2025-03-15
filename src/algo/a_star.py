from queue import PriorityQueue
from util import *
from defs import *

def astar(mp, ghosts_pos, id, pacman_pos, succ_list):
    # Initialize priority queue, dist array, and trace array
    pq = PriorityQueue()  
    dist = []
    trace = [] 
    for i in range(30):
        col = []
        trace_arr = []
        for j in range(33):
            col.append(INF)
            trace_arr.append([-1, -1])
        dist.append(col)
        trace.append(trace_arr)
    
    start = [int(ghosts_pos[id][0]), int(ghosts_pos[id][1])]

    # Push initial state to the priority queue
    # Priority queue's element format: (Estimated cost = f(n) = g(n) + h(n), g(n), node = n)
    init = (get_heuristic(ghosts_pos[id], pacman_pos), 0, start) 
    pq.put(init)
    dist[int(ghosts_pos[id][0])][int(ghosts_pos[id][1])] = get_heuristic(ghosts_pos[id], pacman_pos)

    found = False
    while pq.qsize() > 0: 
        cur = pq.get()

        # Expand goal position -> finish
        if cur[2] == pacman_pos:
            found = True
            break
        
        # Get rid of redundant path
        if cur[0] != dist[cur[2][0]][cur[2][1]]:
            continue
        
        for i in range(4):
            new_pos = [cur[2][0] + dx[i], cur[2][1] + dy[i]]

            # If invalid new position or new position is same as other ghost's current successor, then continue
            if can_go(new_pos, mp) == False:
                continue

            if cur[2] == start and in_succ_list(succ_list, id, new_pos):
                continue
            
            # New h(n) and g(n) of new position
            h = get_heuristic(new_pos, pacman_pos)
            new_dist = cur[1] + 1
            
            # Found more optimized path for new_pos from current position
            if new_dist + h < dist[new_pos[0]][new_pos[1]]:
                pq.put((h + new_dist, new_dist, new_pos))
                dist[new_pos[0]][new_pos[1]] = new_dist + h
                trace[new_pos[0]][new_pos[1]] = cur[2]
    
    # If can't reach, return current position to force ghost to wait
    if not found:
        # print("A* cannot found destination")
        return [start]
        
    # Trace back to find optimal path
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