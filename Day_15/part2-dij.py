import collections
import sys
import time
from collections import defaultdict
from heapq import *
from typing import final

fileName = sys.argv[1]


def parseMyFile(file):
  fileData = open(file, "r")
  lines = fileData.readlines()
  
  rows = []
  
  for line in lines:
    rows.append([[int(char), 0] for char in line.strip()])

  return rows
  
caveMap = parseMyFile(fileName)
print(caveMap)

costs = []
 
def extendMap():
  newMap = []
  for row in caveMap:
    newRow = []
    for i in range(5):
      for char in row:
        count = (char[0] + i) % 9 if (char[0] + i) % 9 > 0 else 9
        newRow.append([count, 0])
        
    newMap.append(newRow)
    
  finalMap = []
  
  for i in range(5):
    for row in newMap:
      newRow = []
      for char in row:
        count = (char[0] + i) % 9 if (char[0] + i) % 9 > 0 else 9
        newRow.append([count, 0])
      finalMap.append(newRow)
    
  return finalMap
      
def printMap(map):
  for row in map:
    for box in row:
      # print(str(box[0]) + "/" + str(box[1]), end=" ")
      print(str(box[0]), end = "")# + "/" + str(box[1]), end=" ")
    
    print("")
  # time.sleep(0.5)
  

def dijkstra(map):
  graph = collections.defaultdict(dict)
  for x in range(len(map)):
    for y in range(len(map[0])):
      graph[x][y] = map[x][y]
     
  print(graph)
  return graph
   
  
print(caveMap[-1][-1])
print(caveMap)
finalMap = extendMap()
dijkstra(finalMap)

printMap(extendMap())

class Graph():
  def __init__(self, dangerLevels):
    self.V = dangerLevels
    self.graph = [[0 for column in dangerLevels] for row in dangerLevels]
    
  def printSolution(self, dist):    
    print("Vertex tDist from Source")
    for node in range(self.V):
      print(node, "t", dist[node])

  # A utility func to find the vertex with min dist val
  # from the set of vertices not yet included in the spt
  def minDistance(self, dist, sptSet):
    # Init min distance for next node
    min = sys.maxsize
    
    # Search not nearest vertex not in the shortest path tree (sptSet)
    for v in range(self.V):
      if dist[v] < min and sptSet[v] == False:
        min = dist[v]
        min_index = v
        
    return min_index
    
  # func that implements Dijistra's single source shortest path algo for a 
  # graph represented using adjancy matrix representation
  def dijkstra(self, src):
    dist = [sys.maxsize] * self.V
    dist[src] = 0
    sptSet = [False] * self.V
    
    for cout in range(self.V):
        # pick the min dist vertex from the set of vertices not yet processed.
        # u is always equal to src in first iteration
        u = self.minDistance(dist, sptSet)
        
        # put the min distance cert in the shortest path tree
        sptSet[u] = True
        
        # Update dist val of the adjacent vertices of the picked vertex only if
        # the current distance is greater than the new distance and the vertex in 
        # not in the shortest path tree
        for v in range(self.V):
          if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
            dist[v] = dist[u] + self.graph[u][v]
            
    self.printSolution(dist)
        
        
  
        
g = Graph(9)

g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]
           
g.dijkstra(0)
