from algo.search import *
from collections import deque
# q.push(start)
# vis[start] = True
# trace[start] = -1
# while q:
#   cur = q.get()
#   for succ of cur:
#       if !vis[succ]:
#           vis[succ] = True
#           trace[succ] = cur
#           q.push(succ)

# trace[x][y] = [pre_x, pre_y]

def bfs(mp, ghosts_pos, id, pacman_pos):
    # Initialize queue, visited, and trace array
    queue = deque()
    visited = []
    trace = []
    start = ghosts_pos[id]
    queue.append(start)


    for x in range(30):
        visited.append([False] * 33)
        trace.append([[-1, -1] for _ in range(33)])

    visited[int(start[0])][int(start[1])] = True
    while queue:
        cur_pos = queue.popleft()

        if cur_pos == pacman_pos:
            break

        for i in range(4):
            new_pos = [cur_pos[0] + dx[i], cur_pos[1]+dy[i]]
            if can_go(new_pos,mp) == False:
                continue

            if not visited[int(new_pos[0])][int(new_pos[1])]:
                queue.append((new_pos))
                visited[int(new_pos[0])][int(new_pos[1])] = True
                trace[int(new_pos[0])][int(new_pos[1])] = cur_pos
    succ = []
    temp = [int(pacman_pos[0]), int(pacman_pos[1])]
    while temp != ghosts_pos[id]:
        succ = temp
        new_temp = trace[int(temp[0])][int(temp[1])]
        temp = new_temp
        # for y in range(33):
        #     trace_arr.append([-1, -1])
        # visited.append(arr)
        # trace.append(trace_arr)
    return succ
    # BFS 
