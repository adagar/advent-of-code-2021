import sys
import time
fileName = sys.argv[1]

def parseMyFile(file):
  fileData = open(file, "r")
  lines = fileData.readlines()
  
  rows = []
  
  for line in lines:
    rows.append([int(char) for char in line.strip()])

  return rows
  
caveMap = parseMyFile(fileName)
print(caveMap)

costs = []

  
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
    def getCost(val):     
      if(val[1] >= 0 and val[1] < len(caveMap[0]) and val[0] >= 0 and val[0] < len(caveMap)):
        return caveMap[val[0]][val[1]]
      else:
        return 100000000
    # surrounding = surrounding.sort(key=getCost)
    
    # print(surrounding)
    for sq in surrounding:
      newY = sq[0]
      newX = sq[1]
      if(newX >= 0 and newX < len(caveMap[0]) and newY >= 0 and newY < len(caveMap) and (len(costs) == 0 or cost + caveMap[newY][newX] < min(costs))):
        explore(sq, cost, False)
        
        
explore((0, 0), 0)
    

  