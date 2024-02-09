# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from graph import Graph

class Test_BFS(unittest.TestCase):

    def aux_test_graph(self, filename_in, filename_out):
        graph = Graph.graph_from_file(filename_in)
        with open(filename_out, "r") as f:
            for line in f.readlines():
                split = line.split(" ")
                src = int(split[0])
                dst = int(split[1])
                if split[2] == "None\n":
                    path = "None"
                else:
                    path = " ".join(split[3:]).strip()
                self.assertEqual(path, str(graph.bfs(src, dst)))
    
    def test_graph1(self):
        self.aux_test_graph("input/graph1.in", "input/graph1.path.out")
    
    def test_graph2(self):
        self.aux_test_graph("input/graph2.in", "input/graph2.path.out")



if __name__ == '__main__':
    unittest.main()
