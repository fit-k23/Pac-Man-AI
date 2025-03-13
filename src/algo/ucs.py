from queue import PriorityQueue
from util import *
from defs import *

def ucs(mp, ghosts_pos, id, pacman_pos):
    # Initialize priority queue and dist array
    pq = PriorityQueue()
    dist = []
    trace = []
    for i in range(30):
        col = []
        trace_col = []
        for j in range(33):
            col.append(INF)
            trace_col.append([-1, -1])
        dist.append(col)
        trace.append(trace_col)

    # Push the initial position to queue
    pq.put( ( 0, [int(ghosts_pos[id][0]), int(ghosts_pos[id][1])] ) )
    dist[int(ghosts_pos[id][0])][int(ghosts_pos[id][1])] = 0
    while pq:
        (cur_dist, cur_pos) = pq.get()
        
        # Get rid of redundant path
        if cur_dist != dist[cur_pos[0]][cur_pos[1]]:
            continue

        # Expand goal position -> end
        if cur_pos == pacman_pos:
            break

        # Check 4 successors
        for i in range(0, 4):
            new_pos = [cur_pos[0] + dx[i], cur_pos[1] + dy[i]]
            if not can_go(new_pos, mp):
                continue
            if dist[new_pos[0]][new_pos[1]] > cur_dist + 1:
                dist[new_pos[0]][new_pos[1]] = cur_dist + 1
                pq.put ( ( dist[new_pos[0]][new_pos[1]], new_pos ))
                trace[new_pos[0]][new_pos[1]] = cur_pos

    # Trace back to find optimal successor
    succ = []
    temp = [int(pacman_pos[0]), int(pacman_pos[1])]
    path = []
    while temp != ghosts_pos[id]:
        succ = temp
        new_temp = trace[temp[0]][temp[1]]
        temp = new_temp
    
    # If succ occupied by other ghost
    occupied = False
    for i in range(0, 4): 
        if ghosts_pos[i] == succ:
            occupied = True

    if occupied:
        for i in range(0, 4):
            new_pos = [ghosts_pos[id][0] + dx[i], ghosts_pos[id][1] + dy[i]]
            if can_go(new_pos, mp) and new_pos != succ:
                path.append(new_pos)
                return path
        path.append(ghosts_pos[id])
        return path
    path.append(succ)
    return path
