# Performance test of the iterative algorithm using cProfile
import cProfile
from Floyd_Algorithms.floyd_iterative_pdf import floyd_iter

# Define INF as 9999 to match the algorithm
INF = 9999

graph = [[0, 7, INF, 8], 
[INF, 0, 5, INF], 
[INF, INF, 0, 2], 
[INF, INF, INF, 0]]


# Performance test using Cprofile
import cProfile
def main():
    floyd_iter(graph)
    
if __name__ == '__main__':
    cProfile.run('main()')