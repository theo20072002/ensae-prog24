# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid
from solver import Solver
import copy


class Test_Put_in_place(unittest.TestCase):

    def test_Put_in_place_grid1(self):
        g = Grid.grid_from_file("input/grid1.in")
        final_state=[list(range(i*g.n+1, (i+1)*g.n+1)) for i in range(g.m)]
        s=Solver()
        s.put_in_place(g,7)
        self.assertEqual(g.state,final_state)
        s.put_in_place(g,1)
        self.assertEqual(g.state,final_state)

    def test_Put_in_place_grid0(self):
        g = Grid.grid_from_file("input/grid0.in")
        final_state=[list(range(i*g.n+1, (i+1)*g.n+1)) for i in range(g.m)]
        s=Solver()
        s.put_in_place(g,0)
        self.assertEqual(g.state, [[1,4],[2,3]])
        s.put_in_place(g,1)
        self.assertEqual(final_state,g.state)

    def test_get_solution_grid0(self):
        g = Grid.grid_from_file("input/grid0.in")
        s=Solver()
        path=s.get_solution(g)
        self.assertEqual(path, [((1, 1), (1, 0)), ((1, 0), (0, 0)), ((1, 0), (1, 1)), ((1, 1), (0, 1))])

    def test_get_solution_grid1(self):
        g = Grid.grid_from_file("input/grid1.in")
        s=Solver()
        path=s.get_solution(g)
        self.assertEqual(path, [((3, 1), (3, 0))])


if __name__ == '__main__':
    unittest.main()

