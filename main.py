from problems import NQueens
from a_star import AStar
from ucs import UCS
from genetic import Genetic

N = 8
# astar = AStar(NQueens(N))
# ucs = UCS(NQueens(N))
# astar.solve().pretty_print()
# ucs.solve().pretty_print()

gen = Genetic(NQueens(N))
gen.solve()