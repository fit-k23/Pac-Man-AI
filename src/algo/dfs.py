from map import Map
from util import *
import random

def dfs(mp: Map, ghosts_pos: list[list[int]], id: int, pacman_pos: list[int], forbid = []) -> list[int]:
    # return ([], 0)
    start: list[int] = [int(ghosts_pos[id][0]), int(ghosts_pos[id][1])]
    maze: list[str] = mp.data

    maze_x = len(maze[0])
    maze_y = len(maze)

    # visited: list[list[int]] = [[False] * maze_y for _ in range(maze_x)] # gen 2D matrix of default False with size (maze_x , maze_y)
    frontier: list[list[int]] = [start]
    visited: list[list[list[int]|None]] = [[None] * maze_y for _ in range(maze_x)]
    visited[start[0]][start[1]] = [-1, -1]

    if forbid != []:
        visited[int(forbid[0])][int(forbid[1])] = [-1, -1]

    # up, down, left, right
    # 0 1 2 3
    # dx = [0, 0, -1, 1]
    # dy = [-1, 1, 0, 0]

    found: bool = False
    _move_set_x = [0, 0, -1, 1]
    _move_set_y = [-1, 1, 0, 0]

    while len(frontier) > 0 and not found:
        current = frontier.pop()
        rdom_succ = [0, 1, 2, 3]
        # If there is a forbidden position, choose successor randomly to avoid cycle
        if forbid != []:
            random.shuffle(rdom_succ)
        for i in range(4):
            _mx = current[0] + _move_set_x[rdom_succ[i]]
            _my = current[1] + _move_set_y[rdom_succ[i]]
            if can_go([_mx, _my], mp) and visited[_mx][_my] is None:
                frontier.append([_mx, _my])
                visited[_mx][_my] = current
                if pacman_pos[0] == _mx and pacman_pos[1] == _my:
                    found = True
                    break
    if not found:
        print("ERROR: destination node is unreachable")
        return []

    if visited[int(pacman_pos[0])][int(pacman_pos[1])] is None:
        return []

    # print(f"visited: {visited}")

    current: list[int] = [int(pacman_pos[0]), int(pacman_pos[1])]

    trace_path: list[list[int]] = []
    while current != start:
        trace_path.append(current)
        _next = visited[current[0]][current[1]]
        # if _next == start:
        # #     print(f"Found path {current}. Source: {_next}")
        #     return current
        current = _next

    trace_path.reverse()
    return trace_path
