# This will work if ran from the root folder ensae-prog24
import sys 
import copy 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid

class Test_performed_swap(unittest.TestCase):
    def test_hashable(self):
        grid = Grid.grid_from_file("input/grid1.in")
        hashed=grid.hashable()
        solution=(1,2,3,4,5,6,8,7)
        self.assertEqual(hashed,solution)

    def test_reciproque(self):
        grid = Grid.grid_from_file("input/grid1.in")
        solution=copy.deepcopy(grid.state)
        hashed=(1,2,3,4,5,6,8,7)
        grid.reciproque(hashed)
        self.assertEqual(grid.state,solution)

if __name__ == '__main__':
    unittest.main()