#A simple implementation of Floyd's algorithm
import itertools

# If there is no path between two nodes, the graph states INF
INF = 9999

graph = [[0, 7, INF, 8], 
[INF, 0, 5, INF], 
[INF, INF, 0, 2], 
[INF, INF, INF, 0]]

MAX_LENGTH = len(graph[0])
# This algorithm will find the shortest route between each vertice in the below matrix
print("Initial graph is below: ")
print(graph)

def floyd_iter(distance): 
# Assume that if start_node and end_node are the same # then the distance would be zero
  for k,i,j in itertools.product(range(MAX_LENGTH),range(MAX_LENGTH), range(MAX_LENGTH)):
    if i == j:
      distance[i][j] = 0 
      continue
# return all possible paths and find the minimum distance
    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j]) 
#Any value that have sys.maxsize has no path
  print(distance) 
  
# Use below function to call shortest distance matrix
print("Below is the output graph which displays the shortest route between each vertice:")
floyd_iter(graph)

# Performance test

import timeit
import time
print("Time in seconds taken to run floyd function is shown below: ")
print(timeit.timeit(stmt='floyd_iter(graph)', setup='' ,number=1, globals=globals()))