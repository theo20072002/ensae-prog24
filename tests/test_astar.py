# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

from graph import Graph
from grid import Grid
from solver import Solver
from time import time

def test_A_star( file_name):
    #pour tester bfs de graph sur les fichiers grid
    s=Solver()
    grid=Grid.grid_from_file( file_name)
    src=grid.state
    final_state=[]
    for i in range(grid.m):
        final_state.append(list(range(i*grid.n+1, (i+1)*grid.n+1)))
    graph=grid.create_graph()
    return s.Astar(grid,src,final_state)

print(test_A_star("input/grid1.in"))