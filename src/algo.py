from util import *
import queue
from queue import PriorityQueue
from defs import *

# Infinity value
INF = 99999

# up, down, left, right
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

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
    
def bfs(mp, ghosts_pos, id, pacman_pos):
    # node = problem.getStartState()
    # frontier = util.queue()
    solution = []
    # visited = []
    # parent = {}
    # node_sol = (0, 0)
    
    # frontier.push(node)
    
    # if problem.isGoalState(node) == True:
    #     return solution
    
    # while frontier.isEmpty() == False:
    #     node = frontier.pop()
        
    #     if problem.isGoalState(node) == True:
    #         #print(node)
    #         node_sol = node
    #         break
        
    #     visited.append(node)
    #     succesors = problem.getSuccesor(node)
        
        
    #     for succesor in succesors:
    #         if succesor not in visited and succesor not in parent:
    #             frontier.push(succesor)
    #             parent[succesor] = node
        
                
            
    # while node_sol in parent and parent[node_sol] != (0, 0):
    #     solution.insert(0, parent[node_sol])
    #     node_sol = parent[node_sol]
    
    return solution

def dfs(mp, ghosts_pos, id, pacman_pos):
    return None

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
            if can_go(new_pos, mp) == False:
                continue
            if dist[new_pos[0]][new_pos[1]] > cur_dist + 1:
                dist[new_pos[0]][new_pos[1]] = cur_dist + 1
                pq.put ( ( dist[new_pos[0]][new_pos[1]], new_pos ))
                trace[new_pos[0]][new_pos[1]] = cur_pos

    # Trace back to find optimal successor
    succ = []
    temp = [int(pacman_pos[0]), int(pacman_pos[1])]
    while temp != ghosts_pos[id]:
        succ = temp
        new_temp = trace[temp[0]][temp[1]]
        temp = new_temp
    
    occupied = False
    for i in range(0, 4): 
        if ghosts_pos[i] == succ:
            occupied = True

    if occupied:
        for i in range(0, 4):
            new_pos = [ghosts_pos[id][0] + dx[i], ghosts_pos[id][1] + dy[i]]
            if can_go(new_pos, mp) and new_pos != succ:
                return new_pos
        return []
    return succ

def astar(mp, ghosts_pos, id, pacman_pos):
    return None
