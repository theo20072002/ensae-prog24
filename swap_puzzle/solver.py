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
        Solves the grid using the A* algorithm, return None if there is no solution
        
        Parameters: 
        -----------
        grid: grid
        node_start: list[list[int]]
        final_state: list[list[int]]
        Output: 
        -------
        path= list[list[list[int]]]
            list of defferents states

        """
        open_dict={} #link an edge of the graph with the needed to reach it from the start 
        grid.state= node_start
        m,n=grid.m, grid.n
        closedList = set()# represente all the edges visited
        Openlist =[] # represente all the edges seen but not visited
        path=[] # the path to go to the solution
        initial_state=Node(m,n,node_start)
        heapq.heappush(Openlist, initial_state)
        open_dict[initial_state.hashable()]=0
        while len (Openlist)>0 :
            curent_state = heapq.heappop(Openlist) #take out the smallest element of openlist 
            closedList.add(curent_state.hashable()) # put the visited edge in closed list
            if curent_state.state==final_state:
                while not curent_state.father is True: # create the path thank's to the dictionnary visited and when the son become True (father of the first state)
                    path.append(curent_state.state)
                    curent_state=curent_state.father
                path.append(curent_state.state)
                path.reverse()# to put the path in the rigth order
                return path 
            
            curent_neighbours= curent_state.neighbour()# give the list of the neighbour of the current state  
            for hashed_neighbour in curent_neighbours: 
                if not(hashed_neighbour in closedList):
                    grid.reciproque(hashed_neighbour) # transform the hashed_ neighbour in matrix : list(list(int))
                    neighbour=Node(m,n,grid.state)
                    cost = curent_state.g + 1 # cost needed to reach the neighbour from the start 
                    if curent_state.g == 0 or open_dict.get(hashed_neighbour,inf)> cost: # if the new cost is smaller than the old one to reach neighbour, or the neigbhour wasn't seen before, we replace is cost with the new one. 
                        neighbour.g = cost
                        neighbour.f = neighbour.g + neighbour.heuristic_manhattan(final_state)
                        neighbour.father = curent_state # allow to keep in memory the father of neigbhour
                        heapq.heappush(Openlist, neighbour)
                        open_dict[hashed_neighbour]=neighbour.g #we replace the new cost to go in the edge neighbour from the start; 
        return None


