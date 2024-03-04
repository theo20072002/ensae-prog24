from grid import Grid
import numpy as np

class Node(Grid):
    def __init__(self,m,n, node=[], father=True):
        Grid.__init__(self,m,n,node)
        self.father = father
        self.g = 0  # Coût depuis le point de départ
        self.h = 0  # Heuristique (estimation du coût jusqu'à l'arrivée)
        self.f = 0  # Coût total (f = g + h)

    def __lt__(self, other):
        return self.f < other.f
    
    def heuristic(self, final_state):
        return np.sum(abs(np.array(final_state)-np.array(self.state)))

