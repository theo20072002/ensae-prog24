from grid import Grid
from time import time
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


class Solver(): 
    """
    A solver class, to be implemented.
    """
    def put_in_place(self,g,k):
        """
        Put the element k of the matrix at it place. raise an error if k isn't in grid 
        Parameters: 
        -----------
        g=Grid
        k=int (in the grid)
        
        Output: 
        -------
        h: list of swap
        """
        
        ligne_k,colone_k=k//g.n,k%g.n #take the position where we want to put k+1
        #we take the place of the current element k+1 in the list and we stock it in the tule cell1
        for i in range(g.m):
            for j in range (g.n):
                if g.state[i][j]==k+1: 
                    cell1=(i,j)
                    break
        h=[]# list of the sequence of swap to put k+1 at it target position
        i,j=cell1 
        # we put k+1 in the good colone first in doing sawp to the right or to the left
        if j<colone_k :
            while j!=colone_k:
                h.append (((i,j),(i,j+1)))
                j+=1
        else :
            while j!=colone_k:
                h.append (((i,j),(i,j-1)))
                j-=1
        # Then we put k+1 in the good line to the bottom or to the top
        if i<ligne_k:
            while i!= ligne_k:
                h.append (((i,colone_k),(i+1,colone_k)))
                i+=1
        else :
            while i!= ligne_k:
                h.append (((i,colone_k),(i-1,colone_k)))
                i-=1
        g.swap_seq(h) # we actualise the current state of our grid after doing our sawp
        return h

    def get_solution(self,g):
        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """

        h=[]
        for k in range(g.n*g.m):
            h+=self.put_in_place(g,k)
        return h


