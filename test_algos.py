import unittest
from Floyd_Algorithms.floyd_iterative_pdf import floyd_iter
from Floyd_Algorithms.floyd_iterative_geek import floydWarshall
from Floyd_Algorithms.floyd_recursive import floyd, sol


#The test needs to prove that both the recursive and iterative functions both return a known expected result from a given input
INF = 9999
input_graph = [[0, 7, INF, 8], [INF, 0, 5, INF], [INF, INF, 0, 2], [INF, INF, INF, 0]]
expected_output = [[0, 7, 12, 8], [INF, 0, 5, 7], [INF, INF, 0, 2], [INF, INF, INF, 0]]


class TestAlgo(unittest.TestCase):
    input_graph = [[0, 7, INF, 8], [INF, 0, 5, INF], [INF, INF, 0, 2], [INF, INF, INF, 0]]

    expected_output = [[0, 7, 12, 8], [INF, 0, 5, 7], [INF, INF, 0, 2], [INF, INF, INF, 0]]

    def test_iterative_pdf_algo(self):
        result = floyd_iter(self.input_graph)
        self.assertEqual(self.input_graph, result)

    def test_iterative_geek_algo(self):
        result = floydWarshall(self.input_graph)
        self.assertEqual(self.input_graph, result)

    #def test_recursive_algo(self):
        #result = floyd(self,k,i,j)
        #self.assertEqual(self.graph, result)
        

if __name__ == '__main__':
    unittest.main()