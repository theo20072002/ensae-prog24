"""
This is the node module. It contains a Node class herited from Grid, created to be used in A* .
"""


from grid import Grid
import numpy as np

class Node(Grid):
    def __init__(self,m,n, node=[], father=True):
        Grid.__init__(self,m,n,node)
        self.father = father
        self.g = 0  # cost form the start
        self.h = 0  # cost estimated by the heuristic
        self.f = 0  # Coût total (f = g + h)

    def __lt__(self, other):
        return self.f < other.f
    
    def __eq__(self, other):
        return self.f == other.f
    
    def heuristic(self, final_state): 
        #heuristic based on the norme1 for the matrix
        return np.sum(abs(np.array(final_state)-np.array(self.state)))/2*self.n # division by 2*n to be sure to under_estimate the path, because each swap reduce the heuristic by max 2*n
    
    def heuristic_manhattan(self,final_state): 
        #heuristic based on the manhattan distance
        
        final_state=[list(range(i*self.n+1,(i+1)*self.n+1)) for i in range(self.m) ]

        row_distance=abs(np.array(self.state)-np.array(final_state))//self.n
        column_distance=abs(np.array(self.state)-np.array(final_state))%self.n
        return np.sum(row_distance+column_distance)/2 # division by 2 to be sure to under_estimate the path, because each swap reduce the heuristic by max 2
    

    


