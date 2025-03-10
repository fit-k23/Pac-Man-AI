import util


dx = [0, -1, 1, 0]
dy = [1, 0, 0, -1]
class SearchProblem:
    def __init__(self, ghost, pacman, mp):
        self.mp = mp
        self.startState = ghost
        self.goalState = pacman
        
    def getStartState(self):
        return self.startState.pos
    
    def isGoalState(self, state):
        if state == self.goalState.pos:
            return True
        return False
    
    def getSuccesor(self, state):
        successes = []
        for i in range(0, 4):
            x_new = state[0] + dx[i]
            y_new = state[1] + dy[i]
            if self.startState.can_go((x_new, y_new), self.mp):
                successes.append((x_new, y_new))                                                     
        return successes
    
    def getCostOfAction(self, action):
        return None



def bfs(problem):
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
                  



def dfs(problem):
    return None

def ucs(problem):
    return None

def astar(problem):
    return None
