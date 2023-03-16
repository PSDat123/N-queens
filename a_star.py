from problems import Problem
import heapq

class AStar:
  class Node:
    def __init__(self, problem: Problem, state, path_cost=0, heuristic=0) -> None:
      self.problem = problem
      self.state = state
      self.h = heuristic
      self.g = path_cost

    def child_node(self, action):
      '''
      Return next node from executing specified action
      '''
      new_state = self.problem.result(self.state, action)
      return AStar.Node(self.problem, new_state, self.g + self.problem.g(self.state, action, new_state), self.problem.h(new_state))

    def pretty_print(self):
      l = len(self.state)
      for i in range(l):
        for j in range(l):
          if i == self.state[j]:
            print("Q ", end='')
          else:
            print("* ", end='')
        print()

    def __repr__(self):
      return f"A* Node {self.state}(g={self.g}, h={self.h})>"

    def __lt__(self, other: 'AStar.Node'):
      return (self.g + self.h) < (other.g + other.h)
    
    def __hash__(self):
      return hash(self.state)

    def __eq__(self, other: 'AStar.Node'):
      return self.state == other.state
    
  def __init__(self, problem: Problem) -> None:
    self.problem = problem
    self.root = AStar.Node(problem, problem.initial_state, 1, problem.h(problem.initial_state))
    
  def solve(self):
    frontier = [self.root]
    heapq.heapify(frontier)
    explored = set()
    explored.add(self.root.state)
    while frontier:
      cur = heapq.heappop(frontier)
      if not cur.h:
        return cur
      for action in self.problem.actions(cur.state):
        new_node = cur.child_node(action) 
        if new_node.state not in explored:
          heapq.heappush(frontier, new_node)
          explored.add(new_node.state)
    return None
