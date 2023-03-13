from abc import ABC, abstractmethod
from random import randrange

class Problem(ABC):
  def __init__(self) -> None:
    self.inital_state = []
  @abstractmethod
  def goal_test(self, state) -> bool:
    '''
    Check if state is final
    '''
    pass

  @abstractmethod
  def actions(self, state):
    '''
    Return available actions
    '''
    pass

  @abstractmethod
  def g(self, cost, from_state, action):
    '''
    Calculate the path cost from one state to another
    '''
    pass

  @abstractmethod
  def h(self, state):
    '''
    Calculate the heuristic of the specified state
    '''
    pass

  @abstractmethod
  def max_h(self):
    '''
    Return the maximum heuristic of the problem
    '''
    pass

  @abstractmethod
  def random_state(self):
    '''
    Return a random state of the problem
    '''
    pass

class NQueens(Problem):
  def __init__(self, n) -> None:
    self.inital_state = tuple([randrange(0, n) for _ in range(n)])
    self.n = n
  
  def check_conflict(self, col1, row1, col2, row2):
    return row1 == row2 or abs(row1 - row2) == abs(col1 - col2)
  
  def goal_test(self, state: 'tuple[int]') -> bool:
    if self.h(state):
      return False
    return True

  def actions(self, state: 'tuple[int]') -> 'tuple[list[int]]':
    actions = []
    for r in range(self.n):
      for c in range(self.n):
        if c != state[r]:
          new_action = list(state[:])
          new_action[r] = c
          actions.append(tuple(new_action))
    return actions

  def g(self, from_state, action) -> int: 
    # Irrelevant
    return 0
  
  def h(self, state: 'tuple[int]'):
    num_conflict = 0
    for i in range(len(state) - 1):
      for j in range(i + 1, len(state)):
        if self.check_conflict(i, state[i], j, state[j]):
          num_conflict += 1
    return num_conflict

  def max_h(self):
    return (self.n * (self.n - 1)) / 2

  def random_state(self) -> 'tuple[int]':
    return tuple([randrange(0, self.n) for _ in range(self.n)])