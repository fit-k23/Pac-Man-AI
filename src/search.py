from algo import *
from map import Map
import tracemalloc

# algo_num: [0->bfs], [1->dfs], [2->ucs], [3->A*]
# A "bridge" class to connect between ghosts and its corresponding search algorithms
# More efficient interface
class Search:
    # Constructor
    def __init__(self, _map: Map, _ghost, _pacman):
        self.map = _map
        self.ghost = _ghost
        self.pacman = _pacman

    # Get the path for corresponding search problems
    # id: id of current ghost
    # ghosts_pos: positions of all ghosts
    # succ_list: lists of successors of all ghosts
    @staticmethod
    def get_path(algo_id, _map: Map, ghosts_pos, id: int, pacman_pos, succ_list):
        match algo_id:
            case 0:
                tracemalloc.start()
                path = bfs(_map, ghosts_pos, id, pacman_pos, succ_list)
                print('BFS memory usage: ', tracemalloc.get_traced_memory())
                tracemalloc.stop()
                return path
            case 1:
                tracemalloc.start()
                path = dfs(_map, ghosts_pos, id, pacman_pos, succ_list)
                print('DFS memory usage: ', tracemalloc.get_traced_memory())
                tracemalloc.stop()
                return path
            case 2:
                tracemalloc.start()
                path = ucs(_map, ghosts_pos, id, pacman_pos, succ_list)
                print('UCS memory usage: ', tracemalloc.get_traced_memory())
                tracemalloc.stop()
                return path
            case 3:
                tracemalloc.start()
                path = astar(_map, ghosts_pos, id, pacman_pos, succ_list)
                print('A* memory usage: ', tracemalloc.get_traced_memory())
                tracemalloc.stop()
                return path