import sys
# from termcolor import colored
 
fileName = sys.argv[1]

def parseMyFile(file):
  fileData = open(file, "r")
  lines = fileData.readlines()
  
  rows = []
  for line in lines:
    rows.append(line.strip().split('-'))
    
  return rows
  
class Node:  
  paths = 0
  
  def __init__(self, name, size):
    self.connections = []
    self.name = name
    self.size = size
    self.visited = False
    
  def addConnection(self, connection):
    # print("ADD CONNECTION")
    # print(self.name, connection, self.connections)
    if(connection not in self.connections and connection.name != self.name):
      # print("NEW CONNECTION")
      self.connections.append(connection)
    # else:
    #   # print("CONNECTION ALREADY EXISTS")
      
  def visit(self):
    if(self.size == "big"):
      return True
    elif(self.name == "start" or self.name == "end"):
      return False
    elif(self.visited == False):
      self.visited = True
      return True
    else:
      return False
      
paths = []
def exploreNodes(node, path = [], doubled = False):
  path.append(node)
  for connection in node.connections:
    if connection.name == "end":
      path.append(connection)
      paths.append(path)
    elif connection.name == 'start':
      continue
    elif connection.size == 'big':
      exploreNodes(connection, path[:], doubled)
    elif connection.size is 'small':
      if connection not in path:
        exploreNodes(connection, path[:], doubled)
      elif doubled == False:
        exploreNodes(connection, path[:], True)
      
      
    
      
  return paths
   
connections = parseMyFile(fileName)

nodes = []
start = None
end = None

for connection in connections:
  # print("### SETUP CONNECTION:", connection)
  nodeA = next(x for x in nodes if x.name == connection[0]) if any(x.name == connection[0] for x in nodes) else Node(connection[0], "small" if connection[0].islower() else "big")
  nodeB = next(x for x in nodes if x.name == connection[1]) if any(x.name == connection[1] for x in nodes) else Node(connection[1], "small" if connection[1].islower() else "big")
  nodeA.addConnection(nodeB)
  nodeB.addConnection(nodeA)
  
  if nodeA not in nodes:
    nodes.append(nodeA)
  if nodeB not in nodes:
    nodes.append(nodeB)
    
  if(nodeA.name == 'start'):
    start = nodeA
  if(nodeB.name == 'end'):
    end = nodeB



paths = exploreNodes(start)
# for node in nodes:
#   print(node.name, ":")
#   for connection in node.connections:
#     print("  ", connection.name)

# print(len(paths))
for path in paths:
  # print (path)
  print("#### PATH ####")
  for node in path:    
    print(node.name)
#   print("")

print(len(paths))
