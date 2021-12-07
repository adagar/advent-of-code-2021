import sys
fileName = sys.argv[1]

def ParseMyFile(file):
  # print("print " + file)
  fileData = open(file, "r")
  lines = fileData.readlines()
  vents = []
  
  for line in lines:    
    newVentData = line[:-1].split(" -> ")
    # print(newVentData)
    newVent = []
    for point in newVentData:
      pointData = point.split(",")
      newVent.append((int(pointData[0]), int(pointData[1])))
    vents.append(newVent)
    
  # print(vents)
  return vents
      
  

vents = ParseMyFile(fileName)
oceanFloor = {}

for vent in vents:
  
  xInit, yInit = vent[0][0], vent[0][1]
  xEnd, yEnd = vent[1][0], vent[1][1]
  
  deltaX = xInit - xEnd
  deltaY = yInit - yEnd
  
  horizontal = deltaY == 0
  vertical = deltaX == 0
  diag = abs(deltaX) == abs(deltaY)
  print("Vent: " + str(vent))# + " " + str(deltaX/abs(deltaX)))# + " " + str(deltaY/abs(deltaY)))
  if horizontal:
    dir = -deltaX/abs(deltaX)
    print("Horizontal")
    for x in range(xInit, xEnd + dir, dir):
      point = (x, yInit)
      if point in oceanFloor:
        oceanFloor[point] += 1
      else:
        oceanFloor[point] = 1
      # print("Point: " + str(point) + ": " + str(oceanFloor[point]))
  elif vertical:
    dir = -deltaY/abs(deltaY)
    print("Vertical")
    for y in range(yInit, yEnd + dir, dir):
      point = (xInit, y)
      if point in oceanFloor:
        oceanFloor[point] += 1
      else:
        oceanFloor[point] = 1
      # print("Point: " + str(point) + ": " + str(oceanFloor[point]))
  elif diag:  
    
    xDir = -deltaX/abs(deltaX)
    yDir = -deltaY/abs(deltaY)
    print("Diagonal" + " " + str(xDir) + " " + str(yDir))
    yCurr = yInit
    for x in range(xInit, xEnd + xDir, xDir):
      
      y = yCurr #yInit - (xInit - x) * yDir
      print("Diag", x, y)
      if(x, y) in oceanFloor:
        oceanFloor[(x, y)] += 1
      else:
        oceanFloor[(x, y)] = 1
        
      yCurr = yCurr + yDir
  print("\n")
count = 0
for key in oceanFloor:
  if oceanFloor[key] > 1:
    count += 1
  
print(count)#, oceanFloor) #, deltaX, deltaY, horizontal, vertical, diag)


