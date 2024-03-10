# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid

class Test_neighbour(unittest.TestCase):
    def test_neighbour(self):
        grid = Grid.grid_from_file("input/grid0.in")
        neighbour=grid.neighbour()
        solution=[(3, 4, 2, 1), (4, 2, 3, 1), (2, 1, 3, 4), (2, 4, 1, 3)]
        self.assertEqual(solution,neighbour)

if __name__ == '__main__':
    unittest.main()