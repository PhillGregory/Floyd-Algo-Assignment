# Performance test of the recursive algorithm using cProfile
import timeit
import cProfile
from Floyd_Algorithms.floyd_recursive import floyd,sol, dist

# Define INF as 9999 to match the algorithm
INF = 9999

graph = [[0, 7, INF, 8], 
[INF, 0, 5, INF], 
[INF, INF, 0, 2], 
[INF, INF, INF, 0]]


# Performance test using Cprofile
import cProfile
def main():
    floyd(0,0,0)
    sol(dist)
    
if __name__ == '__main__':
    cProfile.run('main()')