import sys
from termcolor import colored
 
fileName = sys.argv[1]

def parseMyFile(file):
  fileData = open(file, "r")
  lines = fileData.readlines()
  
  rows = []
  rows.append([9 for i in range(len(lines[0].strip()) + 2)])
  for line in lines:    
    newRow = [9]
    newRow.extend([int(char) for char in line.strip()])
    newRow += [9]
    rows.append(newRow)
  rows.append([9 for i in range(len(lines[0].strip()) + 2)])
  print(rows)
  return rows
  
def isLocalMin(loc, graph):  
    (i, j) = loc
    top = graph[i-1][j] if i > 0 else None
    bottom = graph[i+1][j] if i < len(graph)-1 else None
    left = graph[i][j-1] if j > 0 else None
    right = graph[i][j+1] if j < len(graph[i])-1 else None
    height = graph[i][j]
    return (top is None or height < top) and (bottom is None or height < bottom) and (left is None or height < left) and (right is None or height < right)

def basinLocs(loc, graph):
  basinMembers = [loc]
  (i, j) = loc
  
  surrounding = {
    'top': (i-1,j) if i > 0 else None,
    'bottom': (i+1,j) if i < len(graph)-1 else None,
    'left': (i,j-1) if j > 0 else None,
    'right': (i,j+1) if j < len(graph[i])-1 else None}
  height = graph[i][j]    
    
  for key in surrounding:
    if surrounding[key] is not None:
      x = surrounding[key][0]
      y = surrounding[key][1]
      # print(surrounding[key], "is", key, ":", graph[x][y], height)
      if graph[x][y] > height and graph[x][y] != 9:
        if(x,y) not in basinMembers:
          basinMembers.append((x,y))
          furtherMembers = basinLocs((x,y), graph)
          for member in furtherMembers:
            if member not in basinMembers:
              basinMembers.append(member)
      
  return basinMembers
    
seaFloor = parseMyFile(fileName)

biggestBasins = []
totalBasinMembers = []

for i in range(len(seaFloor)):
  for j in range(len(seaFloor[i])):
    lowPoint = isLocalMin((i,j), seaFloor)
    if lowPoint:
      basinMembers = basinLocs((i,j), seaFloor)
      totalBasinMembers.extend(basinMembers)      
      biggestBasins.append(len(basinMembers))
      # print(biggestBasins)
      
      
for x in range(len(seaFloor)):
  rowStr = ""
  for y in range(len(seaFloor[x])):
    if (x,y) in totalBasinMembers:
      rowStr += colored(str(seaFloor[x][y]), 'red', attrs=['bold'])
    else:
      rowStr += str(seaFloor[x][y])
  print(rowStr)

biggestBasins.sort()
print(biggestBasins[-1] * biggestBasins[-3] * biggestBasins[-2])
