from grid import Grid
from time import time
import heapq
from node import Node
from math import inf

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

    def Astar(self, grid, node_start, final_state):
        """
        Solves the grid using the A* algorithm 
        
        Parameters: 
        -----------
        grid: grid
        node_start: list[list[int]]
        final_state: list[list[int]]

        Output: 
        -------
        grid: Grid
            The grid

        """
        open_dict={}
        grid.state= node_start
        m,n=grid.m, grid.n
        closedList = set()
        Openlist =[]
        path=[]
        initial_state=Node(m,n,node_start)
        heapq.heappush(Openlist, initial_state)
        open_dict[initial_state.hashable()]=0
        while len (Openlist)>0 :
            curent_state = heapq.heappop(Openlist)
            closedList.add(curent_state.hashable())
            if curent_state.state==final_state:
                while not curent_state.father is True: # create the path thank's to the dictionnary visited and when the son become True (father of the first state)
                    path.append(curent_state.state)
                    curent_state=curent_state.father
                path.append(curent_state.state)
                path.reverse()# to put the path in the rigth order
                return path 
            
            curent_neighbours= curent_state.neighbour()
            for hashed_neighbour in curent_neighbours: 
                if not(hashed_neighbour in closedList):
                    grid.reciproque(hashed_neighbour)
                    neighbour=Node(m,n,grid.state)
                    cost = curent_state.g + 1
                    if curent_state.g == 0 or open_dict.get(hashed_neighbour,inf)> cost:
                        neighbour.g = cost
                        neighbour.h = neighbour.heuristic(final_state)
                        neighbour.f = neighbour.g + neighbour.h
                        neighbour.father = curent_state
                        heapq.heappush(Openlist, neighbour)
                        open_dict[hashed_neighbour]=neighbour.g
        return None


