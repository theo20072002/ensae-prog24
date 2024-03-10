# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid
from math import factorial
import random as rd

class Test_create_graph(unittest.TestCase):
    def test_create_graph(self):
        grid = Grid.grid_from_file("input/grid0.in")
        graph=grid.create_graph()
        self.assertEqual(graph.nb_nodes,factorial(grid.m*grid.n))
        self.assertEqual(graph.nb_edges,factorial(grid.m*grid.n)*((grid.m-1)*grid.n+(grid.n-1)*grid.m)/2)
        for i in range (100):
            permutation=[1,2,3,4]
            rd.shuffle(permutation)
            grid.state=[permutation[0:2], permutation[2:]]
            self.assertCountEqual(graph.graph[tuple(permutation)],grid.neighbour() )


if __name__ == '__main__':
    unittest.main()
