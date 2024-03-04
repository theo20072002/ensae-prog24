"""
This is the grid module. It contains the Grid class and its associated methods.
"""
import random
from graph import Graph
import copy
import queue
from time import time
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


# pour definir un fond blanc
cmap_blanc = LinearSegmentedColormap.from_list('blanc', ['#FFFFFF', '#FFFFFF'], N=256)

class Grid():
    """
    A class representing the grid from the swap puzzle. It supports rectangular grids. 

    Attributes: 
    -----------
    m: int
        Number of lines in the grid
    n: int
        Number of columns in the grid
    state: list[list[int]]
        The state of the grid, a list of list such that state[i][j] is the number in the cell (i, j), i.e., in the i-th line and j-th column. 
        Note: lines are numbered 0..m and columns are numbered 0..n.
    """
    
    def __init__(self, m, n, initial_state = []):
        """
        Initializes the grid.

        Parameters: 
        -----------
        m: int
            Number of lines in the grid
        n: int
            Number of columns in the grid
        initial_state: list[list[int]]
            The intiail state of the grid. Default is empty (then the grid is created sorted).
        """
        self.m = m
        self.n = n
        if not initial_state:
            initial_state = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]            
        self.state = initial_state

    def __str__(self): 
        """
        Prints the state of the grid as text.
        """
        output = f"The grid is in the following state:\n"
        for i in range(self.m): 
            output += f"{self.state[i]}\n"
        return output

    def __repr__(self): 
        """
        Returns a representation of the grid with number of rows and columns.
        """
        return f"<grid.Grid: m={self.m}, n={self.n}>"

    def is_sorted(self):
        """
        Checks is the current state of the grid is sorte and returns the answer as a boolean.
        """
        return self.state == [list(range(i*self.n+1, (i+1)*self.n+1)) for i in range(self.m)]

    def swap(self, cell1, cell2):
        """
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed, especially if the cells aren't in the grid.

        Parameters: 
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell. 
        """
        if abs (cell2[0]-cell1[0] )+ abs (cell2[1]-cell1[1] )>1 or not (0<=cell2[0]<self.m and 0<=cell2[1]< self.n and 0<=cell1[0]<self.m and 0<=cell1[1]< self.n): return None
        self.state[cell2[0]][cell2[1]],self.state[cell1[0]][cell1[1]]=self.state[cell1[0]][cell1[1]],self.state[cell2[0]][cell2[1]]

    def swap_seq(self, cell_pair_list):
        """
        Executes a sequence of swaps. 

        Parameters: 
        -----------
        cell_pair_list: list[tuple[tuple[int]]]
            List of swaps, each swap being a tuple of two cells (each cell being a tuple of integers). 
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        for i in range (len (cell_pair_list)):
            cell1, cell2 = cell_pair_list[i]
            self.swap(cell1,cell2)

    @classmethod
    def grid_from_file(cls, file_name): 
        """
        Creates a grid object from class Grid, initialized with the information from the file file_name.
        
        Parameters: 
        -----------
        file_name: str
            Name of the file to load. The file must be of the format: 
            - first line contains "m n" 
            - next m lines contain n integers that represent the state of the corresponding cell

        Output: 
        -------
        grid: Grid
            The grid
        """
        with open(file_name, "r") as file:
            m, n = map(int, file.readline().split())
            initial_state = [[] for i_line in range(m)]
            for i_line in range(m):
                line_state = list(map(int, file.readline().split()))
                if len(line_state) != n: 
                    raise Exception("Format incorrect")
                initial_state[i_line] = line_state
            grid = Grid(m, n, initial_state)
        return grid
    

    def hashable(self):
        """

        transform our grid in an hashable object
        
        Parameters:
        -------
        grid: tuple

        """     
        h=[]
        # create a single list by concatenation of each line of our matrix
        for i in range(self.m):
            h+=self.state[i]
        return tuple(h)

    def reciproque(self,hashe):
        """
        
        transform a tuple of a lsit in a matrix
        
        Output: 
        -------
        hashe: tuple

        """     

        h=[]
        a=list(hashe)
        for i in range(self.m):
            h.append(a[i*self.n:(i+1)*self.n])
        self.state=h

    def neighbour (self) :
        """
        
        return all the neighbour of the state we are in (self.state), if there is no neighbour return []
        
        Output: 
        -------
        hashe: list of tuple

        """     

        m=copy.deepcopy(self.state)
        v=[] # list of all our neighbour
        # to create all the swap possible, we only need to see the swap to the right and the swap to the bottom
        for i in range(self.m):
            for j in range(self.n):
                self.state=copy.deepcopy(m)
                self.swap((i,j),(i+1,j))
                v.append(copy.deepcopy(self.hashable()))#put the hashe of the neighbour in v
                self.state=copy.deepcopy(m)
                self.swap((i,j),(i,j+1))
                v.append(copy.deepcopy(self.hashable()))#put the hashe of the neighbour in v
        self.state=copy.deepcopy(m)
        return v



    def create_graph(self):
        
        """
        
        create the graph of all the permutations possible of our matrix, where the node are the permuation. To do taht, we use a breadth-first search algorithme.
        
        Output: 
        -------
        g: Graph 

        """

        g=Graph([]) #create the graph
        file=queue.Queue() #create the queue of the node we have to explore
        file.put(self.hashable())
        visited={self.hashable()} # create a set of the nodes already seen 
        edges=[]# create the list of all the edges of the graph
        while not file.empty() :
            node1=file.get()# node1 is a node
            self.reciproque(node1)# we put the state of our graphe on the node1 state, to do our swap in neighbour 
            v=self.neighbour()
            for node2 in v:# node2 is a node
                edges.append((node1,node2))
                if node2 not in visited : # if node2 is seen for the first, node2 become visited and it's going to be explore later 
                    visited.add(node2)
                    file.put(node2)
        for edge in edges: #for each edges of our graph, we create the same edge in our graph exept if it was already add in our graph, because (i,j) and (j,i) represente the same edge. 
            node1,node2=edge
            if node2 not in g.graph or node1 not in g.graph[node2]:
                g.add_edge(node1,node2)
        return g

                

    
    def bfs (self):
        """
        
        apply the bfs in creating the graph at the same time to find one of the shortest path to solve the problem 
        
        Output: 
        -------
        path: list of node 

        """
        m,n=self.m, self.n
        file=queue.Queue()#create the queue of the node we have to explore
        file.put(self.hashable())
        visited={self.hashable(): True} # create a dictionnary wich take as kee the son and as value the father of each edges of the graph. the father of scr is True
        final_state=[] #is the hashe of the final matrix 
        path=[]# is the path of our nodes

        #create final state
        for i in range(m):
            final_state +=list(range(i*n+1, (i+1)*n+1))
        final_state=tuple(final_state)


        while not file.empty():#  return nothing if after exploring all our graph we don't find any solution
            node1=file.get()
            self.reciproque(node1) # we put the state of our graphe on the node1 state, to do our swap in neighbour 
            for node2 in self.neighbour():# node2 is one of the node related to a in our graph
                if node2 not in visited : 
                    visited[node2]=node1# we put the son node2 as kee in visited related to the value node1 wich is it father in our graph
                    file.put(node2)
                
                if node2 == final_state:
                    while not node2 is True: # create the path thank's to the dictionnary visited and when the son become True (father of the first state)
                        self.reciproque(node2)# we put the state of node2 on current state of our graphe to put the node of the path on a matrix mode in path  
                        path.append(self.state)
                        node2=visited[node2]
                    path.reverse()# to put the path in the rigth order
                    return path 


    def afficher (self):
        """
        
        draw the current state of grid thank's to imshow from pyplot
        
        Output: 
        -------
        = show self.state

        """
        #to create the grid with a white background 
        plt.imshow(self.state, cmap= cmap_blanc)

        # to put the numeber of each case in the grid
        for i in range(self.m):
            for j in range(self.n):
                plt.text(j, i, str(self.state[i][j]), ha='center', va='center', color='black')

        plt.show()

