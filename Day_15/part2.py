import sys
import time
from typing import final
import heapq
import os
from termcolor import colored

fileName = sys.argv[1]

class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        '''
        This method makes sure that the graph is symmetrical. In other words, if there's a path from node A to B with a value V, there needs to be a path from node B to node A with a value V.
        '''
        graph = {}
        i = 0
        for row in nodes:
          for node in row:
            graph[str(i)] = {}
            i += i
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes
    
    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]
        
def parseMyFile(file):
  fileData = open(file, "r")
  lines = fileData.readlines()
  
  rows = []
  
  for line in lines:
    rows.append([[int(char)] for char in line.strip()])

  return rows
  
caveMap = parseMyFile(fileName)
 
def extendMap():
  extension = 5
  newMap = []
  for row in caveMap:
    newRow = []
    for i in range(extension):
      for char in row:
        count = (char[0] + i) % 9 if (char[0] + i) % 9 > 0 else 9
        newRow.append([count, 0])
        
    newMap.append(newRow)
    
  finalMap = []
  
  for i in range(extension):
    for row in newMap:
      newRow = []
      for char in row:
        count = (char[0] + i) % 9 if (char[0] + i) % 9 > 0 else 9
        newRow.append(count)
      finalMap.append(newRow)
  return finalMap
      
def printMap(map, seen):
  # print(seen)
  clear = lambda: os.system('clear')
  clear()
  for i in range(len(map)):
    rowStr = ""
    for j in range(len(map[0])):
      node = (i, j)
      if node in seen:
        rowStr += colored(str(map[i][j]), 'red', attrs=['bold'])
      else:
        rowStr += colored(str(map[i][j]))
    print(rowStr)

  time.sleep(0.05)
  print('\n\n\n\n')
newMap = extendMap()[:]

#part b
def inRange(loc):
    y = loc[1]
    x = loc[0]
    if y < 0 or y >= len(newMap):
        return False
    row = newMap[y]
    if x < 0 or x >= len(newMap[0]):
        return False
    return True


#part a
def djikstra(graph, start, end):
    queue = [(0, start, None)]
    seen = set()
    
    while True:
        (cost, v, prev) = heapq.heappop(queue)
        if v not in seen:
            seen.add(v)
            printMap(graph, seen)
            if v == end:
                return cost
                
            y = v[0]
            x = v[1]
            next = [(y + 1, x), (y, x + 1), (y - 1, x), (y, x - 1)]  
            for neighbor in next:
                exists = inRange(neighbor)
                if not inRange(neighbor):
                    continue
                else:
                  neighborCost = newMap[neighbor[1]][neighbor[0]]
                  heapq.heappush(queue, (cost + neighborCost, neighbor, v))
  

endPos = (len(newMap)-1,len(newMap[0])-1)
print(djikstra(newMap, (0,0), endPos))
