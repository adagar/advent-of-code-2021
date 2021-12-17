import sys
import time
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

def getCost(val):     
      if(val[1] >= 0 and val[1] < len(caveMap[0]) and val[0] >= 0 and val[0] < len(caveMap)):
        return caveMap[val[0]][val[1]][0]
      else:
        return 100000000
 

def explore(loc, cost, start = True):
  # print(loc)
  (y, x) = loc
  if start is False:
    cost += caveMap[loc[0]][loc[1]]
    
  if len(costs) != 0 and cost > min(costs):
    return
  elif(y == len(caveMap) - 1 and x == len(caveMap[0]) - 1):
    costs.append(cost)
    print(min(costs))
    # time.sleep(1)
    return cost
  else:
    surrounding = [(y + 1, x),
                   (y, x + 1),
                   (y, x - 1),                   
                   (y - 1, x),]
                   
    # print(surrounding)
    
    # surrounding = surrounding.sort(key=getCost)
    
    # print(surrounding)
    for sq in surrounding:
      newY = sq[0]
      newX = sq[1]
      if(newX >= 0 and newX < len(caveMap[0]) and newY >= 0 and newY < len(caveMap) and (len(costs) == 0 or cost + caveMap[newY][newX] < min(costs))):
        explore(sq, cost, False)
        
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
    
# def extendMap()
def aStar(loc, start = False):
  (y, x) = loc
  # print(loc)
  # if start is False:
  # cost += caveMap[loc[0]][loc[1]][0] 
  # if y == len(caveMap) - 1 and x == len(caveMap[0]) - 1:
  #   print("Checking", x, y)
  #   print(caveMap[loc[0]][loc[1]][1])
  # print(x, y)
  
  # printMap()
  # print("\n\n\n")
  initCost = caveMap[y][x][1]
  finalCost = 0
  
  
  prev = [caveMap[y - 1][x][1] if y > 0 else 20000000000, caveMap[y][x - 1][1] if x > 0 else 300000000] if start is False else [0]
  # print(prev, newX, newY)
  if start is False:
    caveMap[y][x][1] = caveMap[y][x][0] + min(prev)
    finalCost = caveMap[y][x][1]
     
  next = [(y + 1, x), (y, x + 1)]
  
  for sq in next:
    newY = sq[0]
    newX = sq[1]
    inRange = newX < len(caveMap[0]) and newY < len(caveMap)
    nextCost = caveMap[newY][newX][1] if inRange else 0
    
    if(newX < len(caveMap[0]) and newY < len(caveMap) and (nextCost == 0 or finalCost > initCost)):
      aStar(sq)
# explore((0, 0), 0)


caveMap = extendMap()

# aStar((0, 0), True)
print(caveMap[-1][-1])
print(caveMap)

printMap(caveMap)

  