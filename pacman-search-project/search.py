# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm 
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  initial_state = problem.getStartState()
  if problem.isGoalState(initial_state):
     return []

  frontier = util.Stack()
  frontier.push((initial_state, []))
  explored = set()

  while not frontier.isEmpty():
    node, path = frontier.pop()
    explored.add(node)
    for child_node, action, cost in problem.getSuccessors(node):
      if child_node not in explored:
        if problem.isGoalState(child_node):
          return path + [action]
        frontier.push((child_node, path+[action]))

def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
  initial_state = problem.getStartState() 
  if problem.isGoalState(initial_state):
     return []

  frontier = util.Queue() 
  frontier.push((initial_state, [])) # FIFO with node as the only element 
  explored = set()

  while not frontier.isEmpty(): 
    node, path = frontier.pop() # Chooses the shallowest node in frontier 
    explored.add(node)
    frontier_list = [frontier_node for (frontier_node, frontier_action) in frontier.list]
    for child_state, action, cost in problem.getSuccessors(node):
      if child_state not in explored or child_state not in frontier_list:
        if problem.isGoalState(child_state):
          return path + [action]
        frontier.push((child_state, path+[action])) 
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  initial_state = problem.getStartState()
  frontier = util.PriorityQueue()
  frontier.push((initial_state, []), 0)
  explored = set()

  while not frontier.isEmpty():
    (node, path) = frontier.pop()
    if problem.isGoalState(node):
      return path
    if node not in explored:
      for child_state, action, child_cost in problem.getSuccessors(node):
        if child_state not in explored:
          frontier.push((child_state, path+[action]), problem.getCostOfActions(path+[action])+child_cost)
    explored.add(node)
  return path

def manhattanHeuristic(position, problem, info={}):
  "The Manhattan distance heuristic for a PositionSearchProblem"
  xy1 = position
  xy2 = problem.goal
  return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=manhattanHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  initial_state = problem.getStartState()
  frontier = util.PriorityQueue()
  frontier.push((initial_state,[]), heuristic(initial_state, problem))
  explored = set()

  while not frontier.isEmpty():
    (node,path) = frontier.pop()
    if problem.isGoalState(node):
      return path
    if node not in explored:
      for child_state, action, cost in problem.getSuccessors(node):
        if child_state not in explored:
          frontier.push((child_state, path+[action]), problem.getCostOfActions(path+[action])+heuristic(child_state, problem))
    explored.add(node)
  return path

    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
