from problems import NQueens
from a_star import AStar
from ucs import UCS
from genetic import Genetic
import tracemalloc
from time import perf_counter_ns

N = 8
TEST_NUM = 3
def benchmark(func):
  def calc():
    t = []
    m = []
    for i in range(TEST_NUM):
      tracemalloc.start()
      t1 = perf_counter_ns()
      print(f"TEST {i + 1}:")
      func()
      t2 = perf_counter_ns()
      peak = tracemalloc.get_traced_memory()[1]
      tracemalloc.stop()
      t.append((t2 - t1) / 10**6)
      m.append(peak / 1024**2)
    print(f"Average time: {sum(t) / TEST_NUM:.2f} ms")
    print(f"Memory usage: {sum(m) / TEST_NUM:.4f} MB")
  return calc


@benchmark
def run_a_star():
  astar = AStar(NQueens(N))
  astar.solve().pretty_print()


@benchmark
def run_ucs():
  ucs = UCS(NQueens(N))
  ucs.solve().pretty_print()

@benchmark
def run_genetic():
  gen = Genetic(NQueens(N))
  gen.solve(1)
  gen.pretty_print()

try:
  N = int(input("Enter number of queens N = "))
except: 
  print("Invalid input!")
  exit()

print("1. A*")
print("2. UCS")
print("3. Genetic algorithm")
try:
  choice = int(input("Your choice: "))
except:
  print("Invalid input")
  exit()

if choice == 1:
  run_a_star()
elif choice == 2:
  run_ucs()
elif choice == 3:
  run_genetic()
