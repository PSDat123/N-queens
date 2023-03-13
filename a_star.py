from problems import Problem
import heapq

class AStar:
  class Node:
    def __init__(self, problem: Problem, state, parent: 'AStar.Node' = None) -> None:
      self.problem = problem
      self.state = state
      self.h = problem.h(state)
      self.g = 0
      self.parent = parent

    # def expand(self):
    #   '''
    #   Return a list of child nodes
    #   '''
    #   return [self.child_node(action) for action in self.problem.actions(self.state)]

    def child_node(self, action):
      '''
      Return next node from executing specified action
      '''
      return AStar.Node(self.problem, action, self)

    def pretty_print(self):
      l = len(self.state)
      for i in range(l):
        for j in range(l):
          if i == self.state[j]:
            print("Q ", end='')
          else:
            print("* ", end='')
        print()

    def get_path(self):
      '''
      Return the path to the current node
      '''
      node, path_back = self, []
      while node:
        path_back.append(node)
        node = node.parent
      path_back.reverse()
      return path_back

    def __repr__(self):
      return f"A* Node {self.state}(g={self.g}, h={self.h})>"

    def __lt__(self, other: 'AStar.Node'):
      return (self.g + self.h) < (other.g + other.h)
  
  def __init__(self, problem: Problem) -> None:
    self.problem = problem
    self.root = AStar.Node(problem, problem.inital_state)
    
  def solve(self):
    frontier = [self.root]
    step = 0
    heapq.heapify(frontier)
    explored = set()
    explored.add(self.root.state)
    while frontier:
      cur = heapq.heappop(frontier)
      print(step, cur.h)
      step += 1
      if not cur.h:
        return cur

      for action in self.problem.actions(cur.state):
        new_node = cur.child_node(action) 
        if new_node.state not in explored:
          heapq.heappush(frontier, new_node)
          explored.add(new_node.state)
    return None
