from map import Map
from util import *
import time

def dfs(mp: Map, ghosts_pos: list[list[int]], id: int, pacman_pos: list[int], succ_list) -> list[list[int]]:
    # elapsed_time = -time.time()

    # Initialize variables and data structures
    # visited[] also plays the trace role
    start: list[int] = [int(ghosts_pos[id][0]), int(ghosts_pos[id][1])]
    maze: list[str] = mp.data

    maze_x = len(maze[0])
    maze_y = len(maze)

    frontier: list[list[int]] = [start]
    visited: list[list[list[int]|None]] = [[None] * maze_y for _ in range(maze_x)]
    visited[start[0]][start[1]] = [-1, -1]

    found: bool = False
    _move_set_x = [0, 0, -1, 1]
    _move_set_y = [-1, 1, 0, 0]

    # Statistics
    start_time = time.time()
    expanded_node = 0

    while frontier and not found:
        current = frontier.pop()
        expanded_node += 1
        # print("pos", current)
        for i in range(4):
            _mx = current[0] + _move_set_x[3 - i]
            _my = current[1] + _move_set_y[3 - i]
            if can_go([_mx, _my], mp) == False or visited[_mx][_my] != None or (current == start and in_succ_list(succ_list, id, [_mx, _my])):
                continue
            # print("succ=",[_mx,_my])
            frontier.append([_mx, _my])
            visited[_mx][_my] = current
            if pacman_pos[0] == _mx and pacman_pos[1] == _my:
                found = True
                break
    end_time = time.time()
    # If goal cannot be reach, return current position to force ghost to wait
    if not found:
        # print("ERROR: destination node is unreachable")
        return [start]

    current: list[int] = [int(pacman_pos[0]), int(pacman_pos[1])]

    # Trace back to find path
    trace_path: list[list[int]] = []
    while current != start:
        trace_path.append(current)
        current = visited[current[0]][current[1]]

    trace_path.reverse()

    del frontier
    del visited

    if not trace_path:
        return [start]
    # print('Path:', trace_path)
    elapsed = end_time - start_time
    # print(f'Time taken DFS: {elapsed:.12f} seconds')
    # print(f'Expanded node:', expanded_node)
    return trace_path
