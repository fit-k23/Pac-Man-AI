from map import Map
from util import *

def dfs(mp: Map, ghosts_pos: list[list[int]], id: int, pacman_pos: list[int], direction = -1) -> list[int]:
    start: list[int] = [int(ghosts_pos[id][0]), int(ghosts_pos[id][1])]
    maze: list[str] = mp.data

    maze_x = len(maze[0])
    maze_y = len(maze)

    # visited: list[list[int]] = [[False] * maze_y for _ in range(maze_x)] # gen 2D matrix of default False with size (maze_x , maze_y)
    frontier: list[list[int]] = [start]
    visited: list[list[list[int]|None]] = [[None] * maze_y for _ in range(maze_x)]
    visited[start[0]][start[1]] = [-1, -1]

    # up, down, left, right
    # 0 1 2 3
    # dx = [0, 0, -1, 1]
    # dy = [-1, 1, 0, 0]

    if direction != -1:
        if direction == 1:
            visited[start[0]][start[1] + 1] = [-1, -1]
        elif direction == 0:
            visited[start[0]][start[1] - 1] = [-1, -1]
        elif direction == 3:
            visited[start[0] - 1][start[1]] = [-1, -1]
        elif direction == 2:
            visited[start[0] + 1][start[1]] = [-1, -1]
    found: bool = False
    # print(f"Pre {prev}\nCur: {start}\n")
    _move_set_x = [0, 0, -1, 1]
    _move_set_y = [-1, 1, 0, 0]

    while len(frontier) > 0 and not found:
        current = frontier.pop()
        for i in range(4):
            _mx = current[0] + _move_set_x[i]
            _my = current[1] + _move_set_y[i]
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

    print(f"visited: {visited}")

    current: list[int] = [int(pacman_pos[0]), int(pacman_pos[1])]
    while current != start:
        _next = visited[current[0]][current[1]]
        if _next == start:
            print(f"Found path {current}. Source: {_next}")
            return current
        current = _next
