import unittest
from Floyd_Algorithms.floyd_iterative_pdf import floyd_iter
from Floyd_Algorithms.floyd_recursive import floyd


#The test needs to prove that both the recursive and iterative functions both return a known expected result from a given input
INF = 9999
input_graph = [[0, 7, INF, 8], [INF, 0, 5, INF], [INF, INF, 0, 2], [INF, INF, INF, 0]]
expected_output = [[0, 7, 12, 8], [INF, 0, 5, 7], [INF, INF, 0, 2], [INF, INF, INF, 0]]

class TestAlgo(unittest.TestCase):

    def test_iterative_algo(self):
        result = Floyd_Algorithms.floyd_iterative_pdf.floyd_iter(self,input_graph)
        self.assertIs(input_graph == expected_output)

    def test_recursive_algo(self):
        result = Floyd_Algorithms.floyd_iterative_pdf.floyd_iter(self,input_graph)
        self.assertIs(input_graph == expected_output)
        

if __name__ == '__main__':
    unittest.main()

