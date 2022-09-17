from math import dist
import unittest
from floyd_recursive import floyd, sol, dist
from floyd_iterative import floydWarshall, printSolution
INF = 9999
graph = [[0, 7, INF, 8], [INF, 0, 5, INF], [INF, INF, 0, 2], [INF, INF, INF, 0]]
V = len(graph[0])

class Testalgo(unittest.TestCase):

    def Test_algo(self):
        self.assertIs(len(dist), len(graph))

if __name__ == '__main__':
    unittest.main()

