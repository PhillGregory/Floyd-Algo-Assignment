# Python Recursive version of Floyd Marshall Algorithm

# If there is no path between two nodes, the graph states INF. INF is defined below as a large integer.
INF = 9999

# If the start node is the same as the end node, the distance is 0

# This algorithm will find the shortest route between each vertice in the below matrix
print("Initial graph is below: ")

graph = [[0, 7, INF, 8], 
[INF, 0, 5, INF], 
[INF, INF, 0, 2], 
[INF, INF, INF, 0]]

print(graph)

# V represents the number of vertices in the graph
V = len(graph[0])

# Define dist variable as below (similarly to the dist function in floyd_iterative_geek.py)
dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

# Algorithm
def floyd(k,i,j):
  # Now check each vertice individually using recursion
  if k < V and i < V and j < V:
      dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
      k+=1
      return floyd(k,i,j)

  elif i < V and j < V:
      k=0
      dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
      i+=1
      return floyd(k,i,j)

  elif j < V:
      i=0
      k=0
      dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
      j+=1
      return floyd(k,i,j)

# Function for the distance solution
def sol(dist):
    if i < V:
        i+=1
        if(dist[i][j] == INF):
            print("%7s" % ("INF"), end=" ")
    elif j < V:
        j+=1
        if(dist[i][j] == INF):
            print("%7s" % ("INF"), end=" ")
    else:
        print("%7d\t" % (dist[i][j]), end=' ')
    print(" ")

# Use below function to call shortest distance matrix
print("Below is the output graph which displays the shortest route between each vertice:")
floyd(0,0,0)
print(dist)
