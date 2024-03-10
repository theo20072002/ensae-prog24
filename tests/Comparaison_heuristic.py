# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")


from grid import Grid
from solver import Solver
from time import time
from node import Node
import random as rd
import copy

def test_A_star( file_name, heuristic):
    # test bfs from graph on grid.in
    s=Solver()
    grid=Grid.grid_from_file( file_name)
    return s.Astar(grid,heuristic)

def test_get_solution( file_name):
    # test bfs from graph on grid.in
    s=Solver()
    grid=Grid.grid_from_file( file_name)
    return s.get_solution(grid)



#comparison of calculation time depending on the heuristic 
for i in range(5):
    t=time()
    path = test_A_star("input/grid"+str(i)+".in", "heuristic_norme1")
    print("le temps de calcul pour norme1 est : "+str(time()-t)+ " et le nombre de sommmet visiter est "+str(path[1]) )
    t=time()
    path = test_A_star("input/grid"+str(i)+".in", "heuristic_manhattan")
    print("le temps de calcul pour manhattan est : "+str(time()-t)+" et le nombre de sommmet visiter est "+str(path[1]))
    t=time()
    path = test_A_star("input/grid"+str(i)+".in", "heuristic_manhattan")
    print("le temps de calcul pour manhattan2 est : "+str(time()-t)+" et le nombre de sommmet visiter est "+str(path[1]))
    t=time()
    path = test_get_solution("input/grid"+str(i)+".in")
    print("le temps de calcul pour get_solution est : "+str(time()-t))
                            
#comparison of path side depending on the heuristic
m, n = 4, 4
N = 1000
sum_l1 = 0
sum_man = 0
sum_man2=0
for i in range(N):
    random_node = Node(m, n)
    random_node.random()
    sum_l1 += random_node.heuristic_norme1() / N
    sum_man += random_node.heuristic_manhattan() / N
    sum_man2+=random_node.heuristic_manhattan2() / N
print(sum_man, sum_l1,sum_man2)

#time to solve a 5,5 array thank's to manhattan3
s=Solver()
random_node=Node(5,5)
random_node.random()
state=copy.deepcopy(random_node.state)
t=time()
path=s.Astar(random_node, "heuristic_manhattan3")
print("le nombre de coup,  pour manhattan3,  est de "+ str(len(path[0])-1)+ "et le temps de calcul est de" + str(time()-t))
random_node.state=state
s.get_solution(random_node)
print("le nombre de coup, pour get solution,  est de "+ str(len(path[0])-1)+ "et le temps de calcul est de" + str(time()-t))
