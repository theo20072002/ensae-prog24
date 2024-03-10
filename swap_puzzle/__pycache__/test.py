
import sys 
sys.path.append("swap_puzzle/")
import node
import random
from solver import Solver
import random as rd
from grid import Grid
"""
m, n = 4, 4
N = 1000
sum_l1 = 0
sum_man = 0
final_state = [[n * i + j + 1 for j in range(n)] for i in range(m)]
for i in range(N):
    state = [*range(1, m*n+1)]
    random.shuffle(state)
    state = [[state[n * i + j] for j in range(n)] for i in range(m)]
    random_node = node.Node(m, n, state)
    sum_l1 += random_node.heuristic(final_state) / N
    sum_man += random_node.heuristic_manhattan(final_state) / N

print(sum_man, sum_l1)"""

m=4
n=4
final_state=[[i+1 for i in range(j*n,(j+1)*n)] for j in range(m)]
random_permutation=list(range(1,m*n+1))
rd.shuffle(random_permutation)
board=[]
for i in range (m):
    board.append(random_permutation[i*n:(i+1)*n])

s=Solver()
grid=Grid(m,n,board)
solution_state=s.Astar(grid,board,final_state)
print(len(solution_state))