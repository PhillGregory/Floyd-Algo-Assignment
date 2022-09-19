# Unit tests will be carried out below to test the Floyd function in floyd_recursive

#First import the unittest module and the relevant floyd function
import unittest
from Floyd_Algorithms.floyd_recursive import floyd, sol

# Define INF as 9999 to match the algorithm
INF = 9999

# Test case used in algorithm build
input_graph1 = [[0, 7, INF, 8], [INF, 0, 5, INF], [INF, INF, 0, 2], [INF, INF, INF, 0]]
expected_output1 = [[0, 7, 12, 8], [INF, 0, 5, 7], [INF, INF, 0, 2], [INF, INF, INF, 0]]

# Test case that includes negative edges
input_graph2 = [[0, 1, INF, INF], [INF, 0, -1, INF], [INF, INF, 0, -1], [-1, INF, INF, 0]]
expected_output2 = [[0, -1, -2, -1], [-3, 0, -3, -2], [-2, -1, 0, -1], [-1, 0, -1, 0]]

# Test case with vertices greater than 4. To show that the algorithm works for larger graphs
input_graph3 = [[0, 7, INF, 8, 4], [INF, 0, 5, INF, 3], [INF, INF, 0, 2, 6], [INF, INF, 2, 0, 4], [INF, INF, INF, INF, 0]]
expected_output3 = [[0, 7, 10, 8, 4], [INF, 0, 5, 7, 3], [INF, INF, 0, 2, 6], [INF, INF, 2, 0, 4], [INF, INF, INF, INF, 0]]

# Unit tests below to test the imported floyd recursive algorithm using the unittest module. 
# Each test represents a different graph input
class TestRec(unittest.TestCase):
    def test_floyd_rec1(self):
        self.assertEqual(floyd(input_graph1), expected_output1)
        
    def test_floyd_rec2(self):
        self.assertEqual(floyd(input_graph2), expected_output2)
        
    def test_floyd_rec3(self):
        self.assertEqual(floyd(input_graph3), expected_output3)

# The below code is used to run this test script
if __name__ == '__main__':
    unittest.main()