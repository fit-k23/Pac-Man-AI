from queue import PriorityQueue
from util import *
from defs import *

def ucs(mp, ghosts_pos, id, pacman_pos, succ_list):
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

    start = [int(ghosts_pos[id][0]), int(ghosts_pos[id][1])]

    # Push the initial position to queue
    pq.put( ( 0, start ) )
    dist[int(ghosts_pos[id][0])][int(ghosts_pos[id][1])] = 0

    # if forbid:
    #     print("ucs ", forbid)

    found = False
    cnt_loop = 0
    # print("Entering ucs")
    while pq.qsize() > 0:
        (cur_dist, cur_pos) = pq.get()
        
        # Get rid of redundant path
        if cur_dist != dist[cur_pos[0]][cur_pos[1]]:
            continue

        # Expand goal position -> end
        if cur_pos == pacman_pos:
            found = True
            break

        # Check 4 successors
        for i in range(0, 4):
            new_pos = [cur_pos[0] + dx[i], cur_pos[1] + dy[i]]
            if not can_go(new_pos, mp) or (cur_pos == start and in_succ_list(succ_list, id, new_pos)):
                continue
            if dist[new_pos[0]][new_pos[1]] > cur_dist + 1:
                dist[new_pos[0]][new_pos[1]] = cur_dist + 1
                pq.put ( ( dist[new_pos[0]][new_pos[1]], new_pos ))
                trace[new_pos[0]][new_pos[1]] = cur_pos
        cnt_loop += 1
        if cnt_loop >= 600:
            print("ucs wrong")
            break
    # print("Exit ucs")
    if not found:
        # print("ucs cannot reach destination")
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
        # print("ucs cannot reach destination")
        path = [start]
    # print("found path", path)
    return path
