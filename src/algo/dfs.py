from map import Map
from util import *
import random

def dfs(mp: Map, ghosts_pos: list[list[int]], id: int, pacman_pos: list[int], succ_list) -> list[list[int]]:
    # if forbid is None:
    #     forbid = []
    start: list[int] = [int(ghosts_pos[id][0]), int(ghosts_pos[id][1])]
    maze: list[str] = mp.data

    maze_x = len(maze[0])
    maze_y = len(maze)

    frontier: list[list[int]] = [start]
    visited: list[list[list[int]|None]] = [[None] * maze_y for _ in range(maze_x)]
    visited[start[0]][start[1]] = [-1, -1]

    found: bool = False
    _move_set_x = [0, 0, -1, 1]
    _move_set_y = [1, -1, 0, 0]
    cnt_loop = 0

    while frontier and not found:
        current = frontier.pop()
        for i in range(4):
            _mx = current[0] + _move_set_x[i]
            _my = current[1] + _move_set_y[i]
            if can_go([_mx, _my], mp) == False or visited[_mx][_my] != None or (current == start and in_succ_list(succ_list, id, [_mx, _my])):
                continue

            frontier.append([_mx, _my])
            visited[_mx][_my] = current
            if pacman_pos[0] == _mx and pacman_pos[1] == _my:
                found = True
                break
        cnt_loop += 1
        if cnt_loop >= 600:
            print("dfs wrong")
            break

    if not found:
        # print("ERROR: destination node is unreachable")
        return [start]

    current: list[int] = [int(pacman_pos[0]), int(pacman_pos[1])]

    trace_path: list[list[int]] = []
    while current != start:
        trace_path.append(current)
        current = visited[current[0]][current[1]]

    trace_path.reverse()

    del frontier
    del visited

    if trace_path == []:
        trace_path = [start]

    return trace_path
