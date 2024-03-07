# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

from graph import Graph
from grid import Grid
from solver import Solver
from time import time

# partie 1 dedier au 2 premiers TD:

def test_grid1( file_name):
    #pour tester get_solution sur les fichiers grid
    grid=Grid.grid_from_file( file_name)
    s=Solver()
    return s.get_solution(grid)

def test_grid2( file_name):
    #pour tester bfs de graph sur les fichiers grid
    grid=Grid.grid_from_file( file_name)
    src=grid.hashable()
    final_state=[]
    for i in range(grid.m):
        final_state +=list(range(i*grid.n+1, (i+1)*grid.n+1))
    dst=tuple(final_state)
    graph=grid.create_graph()
    return graph.bfs(src,dst)


def test_grid3( file_name):
    #pour tester bfs de grid sur les fichiers grid
    grid=Grid.grid_from_file( file_name)
    return grid.bfs()

#pour evaluer le temps de calcule de get_solution
for i in range(5):
    t=time()
    print(test_grid1("input/grid"+str(i)+".in"))
    print(time()-t)

#pour verifier si le cheminde de get_solution est minimal :
for i in range(3):
    if len(test_grid1("input/grid"+str(i)+".in"))>len(test_grid3("input/grid"+str(i)+".in")):
        print("la solution n'est pas minimale")
    else : print("la solution est minimale")

#pour tester bfs de grid
print(test_grid3("input/grid"+str(4)+".in"))

