from util import *
import queue
from queue import PriorityQueue
from defs import *
from algo.a_star import *
from algo.dfs import *
from algo.bfs import *
from algo.ucs import *

# algo_num: [0->bfs], [1->dfs], [2->ucs], [3->A*]
class Search:
    # Constructor
    def __init__(self, _mp, _ghost, _pacman):
        self.mp = _mp
        self.ghost = _ghost
        self.pacman = _pacman

    # Get best successor with current problem state
    # id: id of current ghost
    # ghosts_pos: positions of all ghosts
    @staticmethod
    def get_optimal_successor(algo_id, mp, ghosts_pos, id, pacman_pos):
        match algo_id:
            case 0:
                return bfs(mp, ghosts_pos, id, pacman_pos)
            case 1:
                return dfs(mp, ghosts_pos, id, pacman_pos)
            case 2:
                return ucs(mp, ghosts_pos, id, pacman_pos)
            case 3:
                return astar(mp, ghosts_pos, id, pacman_pos)