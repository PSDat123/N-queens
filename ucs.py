from problems import Problem
import heapq


class UCS:
  class Node:
    def __init__(self, problem: Problem, state, parent: 'UCS.Node' = None, path_cost=0) -> None:
      self.problem = problem
      self.state = state
      self.h = 0
      self.g = path_cost
      self.parent = parent

    def child_node(self, action):
      '''
      Return next node from executing specified action
      '''
      return UCS.Node(self.problem, action, self, self.g + 1)

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
      return f"UCS Node {self.state}(g={self.g}, h={self.h})>"

    def __lt__(self, other: 'UCS.Node'):
      return self.g < other.g

  def __init__(self, problem: Problem) -> None:
    self.problem = problem
    self.root = UCS.Node(problem, problem.inital_state)

  def solve(self):
    frontier = [self.root]
    step = 0
    heapq.heapify(frontier)
    explored = set()
    while frontier:
      cur = heapq.heappop(frontier)
      if self.problem.goal_test(cur.state):
        print(cur.get_path())
        return cur
      if cur.state in explored:
        continue

      step += 1
      explored.add(cur.state)
      for action in self.problem.actions(cur.state):
        new_node = cur.child_node(action)
        if new_node.state not in explored:
          heapq.heappush(frontier, new_node)
    return None
