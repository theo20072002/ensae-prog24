# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid
from solver import Solver
import copy


class Test_Astar(unittest.TestCase):

    def test_Astar_grid1(self):
        g = Grid.grid_from_file("input/grid1.in")
        initial_state=copy.deepcopy(g.state)
        final_state=[list(range(i*g.n+1, (i+1)*g.n+1)) for i in range(g.m)]
        s=Solver()
        path=s.Astar(g)
        self.assertEqual(len(path)-1,1)
        sequence=g.performed_swap_seq(path)
        g.state=copy.deepcopy(path[0])
        self.assertEqual(initial_state,g.state)
        g.swap_seq(sequence)
        self.assertEqual(g.state,final_state)

    def test_Astar_grid0(self):
        g = Grid.grid_from_file("input/grid0.in")
        initial_state=copy.deepcopy(g.state)
        final_state=[list(range(i*g.n+1, (i+1)*g.n+1)) for i in range(g.m)]
        s=Solver()
        path=s.Astar(g)
        self.assertEqual(len(path)-1,2)
        sequence=g.performed_swap_seq(path)
        g.state=copy.deepcopy(path[0])
        self.assertEqual(initial_state,g.state)
        g.swap_seq(sequence)
        self.assertEqual(g.state,final_state)

if __name__ == '__main__':
    unittest.main()
