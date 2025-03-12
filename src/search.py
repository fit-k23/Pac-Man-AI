from algo import *
from map import Map

# algo_num: [0->bfs], [1->dfs], [2->ucs], [3->A*]
class Search:
    # Constructor
    def __init__(self, _map: Map, _ghost, _pacman):
        self.map = _map
        self.ghost = _ghost
        self.pacman = _pacman

    # Get the best successor with current problem state
    # id: id of current ghost
    # ghosts_pos: positions of all ghosts
    @staticmethod
    def get_optimal_successor(algo_id, _map: Map, ghosts_pos, id: int, pacman_pos, direction = -1):
        match algo_id:
            case 0:
                return bfs(_map, ghosts_pos, id, pacman_pos)
            case 1:
                return dfs(_map, ghosts_pos, id, pacman_pos, )
            case 2:
                return ucs(_map, ghosts_pos, id, pacman_pos)
            case 3:
                return astar(_map, ghosts_pos, id, pacman_pos)