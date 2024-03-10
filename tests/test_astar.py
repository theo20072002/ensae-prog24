# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

from graph import Graph
from grid import Grid
from solver import Solver
import cProfile
from time import time

def test_A_star( file_name):
    #pour tester bfs de graph sur les fichiers grid
    s=Solver()
    grid=Grid.grid_from_file( file_name)
    src=grid.state
    final_state=[]
    for i in range(grid.m):
        final_state.append(list(range(i*grid.n+1, (i+1)*grid.n+1)))
    return s.Astar(grid,src,final_state)

path = test_A_star("input/grid4.in")
swap_path = []
initial_grid = Grid.grid_from_file("input/grid4.in")
grid = Grid.grid_from_file("input/grid4.in")
n = 0
for i in range(len(path) - 1):
    grid.state = path[i]
    swap = grid.give_perform_swap(path[i+1])
    swap_path.append(swap)
    n += 1
initial_grid.swap_seq(swap_path)
print(initial_grid)