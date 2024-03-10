from grid import Grid
from time import time
import heapq
from node import Node
from math import inf
import queue

class Solver(): 
    """
    A solver class, to be implemented.
    """
    def put_in_place(self,g,k):
        """
        Put the element k of the matrix at it place, 1 is the element 0. raise an error if k isn't in grid 
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



    def bfs (self,grid):
        """
        
        apply the bfs in creating the graph at the same time to find one of the shortest path to solve the problem 
        
        Parameters: 
        -----------
        g=Grid

        Output: 
        -------
        path: list of node 

        """
        m,n=grid.m, grid.n
        file=queue.Queue()#create the queue of the node we have to explore
        file.put(grid.hashable())
        visited={grid.hashable(): True} # create a dictionnary wich take as kee the son and as value the father of each edges of the graph. the father of scr is True
        final_state=[] #is the hashe of the final matrix 
        path=[]# is the path of our nodes

        #create final state
        for i in range(m):
            final_state +=list(range(i*n+1, (i+1)*n+1))
        final_state=tuple(final_state)


        while not file.empty():#  return nothing if after exploring all our graph we don't find any solution
            node1=file.get()
            grid.reciproque(node1) # we put the state of our graphe on the node1 state, to do our swap in neighbour 
            for node2 in grid.neighbour():# node2 is one of the node related to a in our graph
                if node2 not in visited : 
                    visited[node2]=node1# we put the son node2 as kee in visited related to the value node1 wich is it father in our graph
                    file.put(node2)
                
                if node2 == final_state:
                    while not node2 is True: # create the path thank's to the dictionnary visited and when the son become True (father of the first state)
                        grid.reciproque(node2)# we put the state of node2 on current state of our graphe to put the node of the path on a matrix mode in path  
                        path.append(grid.state)
                        node2=visited[node2]
                    path.reverse()# to put the path in the rigth order
                    return path


    def Astar(self, grid, heuristic):
        """
        Solves the grid using the A* algorithm, return None if there is no solution
        
        Parameters: 
        -----------
        grid: grid
        heuristic : str
        
        Output: 
        -------
        path= list[list[list[int]]]
            list of defferents states

        """
        open_dict={} #link an edge of the graph with the needed to reach it from the start 
        m,n=grid.m, grid.n
        final_state=[list(range(i*n+1, (i+1)*n+1)) for i in range(m)]
        closedList = set()# represente all the edges visited
        Openlist =[] # represente all the edges seen but not visited
        path=[] # the path to go to the solution
        initial_state=Node(m,n,grid.state)
        heapq.heappush(Openlist, initial_state)
        open_dict[initial_state.hashable()]=0
        while len (Openlist)>0 :
            current_state = heapq.heappop(Openlist) #take out the smallest element of openlist 
            closedList.add(current_state.hashable()) # put the visited edge in closed list
            if current_state.state==final_state:
                while not current_state.father is True: # create the path thank's to the dictionnary visited and when the son become True (father of the first state)
                    path.append(current_state.state)
                    current_state=current_state.father
                path.append(current_state.state)
                path.reverse()# to put the path in the rigth order
                return path, len(closedList)
            
            current_neighbours= current_state.neighbour()# give the list of the neighbour of the current state  
            for hashed_neighbour in current_neighbours: 
                if not(hashed_neighbour in closedList):
                    grid.reciproque(hashed_neighbour) # transform the hashed_ neighbour in matrix : list(list(int))
                    neighbour=Node(m,n,grid.state)
                    cost = current_state.g + 1 # cost needed to reach the neighbour from the start 
                    if current_state.g == 0 or open_dict.get(hashed_neighbour,inf)> cost: # if the new cost is smaller than the old one to reach neighbour, or the neigbhour wasn't seen before, we replace is cost with the new one. 
                        neighbour.g = cost
                        neighbour.f = neighbour.g + getattr(neighbour,heuristic)()
                        neighbour.father = current_state # allow to keep in memory the father of neigbhour
                        heapq.heappush(Openlist, neighbour)
                        open_dict[hashed_neighbour]=neighbour.g #we replace the new cost to go in the edge neighbour from the start; 
        return None


