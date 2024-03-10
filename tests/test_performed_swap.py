# This will work if ran from the root folder ensae-prog24
import sys 
import copy 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid

class Test_performed_swap(unittest.TestCase):
    def test_performed_swap(self):
        grid = Grid.grid_from_file("input/grid1.in")
        initial_state=copy.deepcopy(grid.state)
        grid.swap((2,1),(1,1))
        swap=grid.performed_swap(initial_state)
        self.assertIn(swap,[((1,1),(2,1)),((2,1),(1,1))])

    def test_performed_swap_seq(self):
        sequence=[((3,0), (3,1)), ((3,0), (3,1)),((2,1),(3,1))]
        permutation_sequence=[]
        for i in range (len(sequence)):
            if sequence[i][0][0]>sequence[i][1][0] or ( sequence[i][0][0]==sequence[i][1][0] and sequence[i][0][1]>sequence[i][1][1]):
                permutation_sequence.append((sequence[i][1],sequence[i][0]))
            else :
                permutation_sequence.append(sequence[i])
        path=[]
        grid = Grid.grid_from_file("input/grid1.in")
        path.append(copy.deepcopy(grid.state))
        for i in sequence :
            grid.swap(i[0],i[1])
            path.append(copy.deepcopy(grid.state))
        swap_seq=grid.performed_swap_seq(path)
        self.assertEqual(swap_seq,permutation_sequence)

if __name__ == '__main__':
    unittest.main()
