from abc import ABC, abstractmethod
from random import randrange
import itertools

class Problem(ABC):
  def __init__(self) -> None:
    self.initial_state = []
    self.n = 0
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
  def result(self, state, action):
    '''
    Return state created from an action
    '''
    pass

  @abstractmethod
  def g(self, from_state, action, to_state):
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
  def random_state(self):
    '''
    Return a random state of the problem
    '''
    pass

class NQueens(Problem):
  def __init__(self, n) -> None:
    self.initial_state = tuple([randrange(0, n) for _ in range(n)])
    self.n = n
  
  def check_conflict(self, col1, row1, col2, row2):
    return row1 == row2 or abs(row1 - row2) == abs(col1 - col2)
  
  def goal_test(self, state: 'tuple[int]') -> bool:
    return not self.h(state)
  
  def actions(self, state: 'tuple[int]') -> 'tuple[int]':
    return itertools.filterfalse(lambda x: x[1] == state[x[0]], itertools.product(range(self.n), repeat=2))
  
  def result(self, state, action):
    new_state = list(state)
    new_state[action[0]] = action[1]
    return tuple(new_state)

  def g(self, from_state, action, to_state) -> int: 
    return 1
  
  def h(self, state: 'tuple[int]'):
    num_conflict = 0
    for i in range(len(state) - 1):
      for j in range(i + 1, len(state)):
        if self.check_conflict(i, state[i], j, state[j]):
          num_conflict += 1
    return num_conflict

  def random_state(self) -> 'tuple[int]':
    return tuple([randrange(0, self.n) for _ in range(self.n)])
