"""
This is the grid module. It contains the Grid class and its associated methods.
"""

import random
from graph import Graph
import copy
import queue

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
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed.

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
        h=[]
        for i in range(self.m):
            h+=self.state[i]
        return tuple(h)

    def reciproque(self,hashe):
        h=[]
        a=list(hashe)
        for i in range(self.m):
            h.append(a[i*self.n:(i+1)*self.n])
        self.state=h

    def voisin (self) :
        m=copy.deepcopy(self.state)
        v=[]
        for i in range(self.m):
            for j in range(self.n):
                self.state=copy.deepcopy(m)
                self.swap((i,j),(i+1,j))
                v.append(copy.deepcopy(self.hashable()))
                self.state=copy.deepcopy(m)
                self.swap((i,j),(i,j+1))
                v.append(copy.deepcopy(self.hashable()))
        self.state=copy.deepcopy(m)
        return v



    def create_graph(self):
        g=Graph([])
        file=queue.Queue()
        file.put(self.hashable())
        visited={self.hashable()}
        edges=[]
        while not file.empty() :
            node1=file.get()
            self.reciproque(node1)
            v=self.voisin()
            for node2 in v:
                edges.append((node1,node2))
                if node2 not in visited : 
                    visited.add(node2)
                    file.put(node2)
        for edge in edges:
            node1,node2=edge
            if node2 not in self.graph or node1 not in self.graph[node2]:
                g.add_edge(node1,node2)
        return g

                

    
    def bfs (self):
        m,n=self.m, self.n
        file=queue.Queue()
        file.put(self.hashable())
        visited={self.hashable(): True}
        final_state=[]
        path=[]

        for i in range(m):
            final_state +=range(i*n+1, (i+1)*n+1)
        final_state=list(final_state)

        while not file.empty():
            node1=file.get()
            self.reciproque(node1)
            v=self.voisin()
            for node2 in v:
                if node2 not in visited : 
                    visited[node2]=node1
                    file.put(node2)
                if node2 == final_state:

                    
                    while not node2 is True: 
                        path.append(node2)
                        node2=visited[node2]
                    path.reverse()
                    return path 

d= Grid(4,4,[])
print(d.is_sorted())
d.swap((1,2),(2,2))
print(d)

d.swap_seq([((3,2),(2,2)),((4,2),(3,2))])
