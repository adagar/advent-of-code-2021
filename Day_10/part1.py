import sys
fileName = sys.argv[1]

def parseMyFile(file):
  fileData = open(file, "r")
  lines = fileData.readlines()
  
  rows = []
  for line in lines:    
    rows.append([int(char) for char in line.strip()])
  
  return rows
  
danger = 0
seaFloor = parseMyFile(fileName)

for i in range(len(seaFloor)):
  for j in range(len(seaFloor[i])):
    top = seaFloor[i-1][j] if i > 0 else None
    bottom = seaFloor[i+1][j] if i < len(seaFloor)-1 else None
    left = seaFloor[i][j-1] if j > 0 else None
    right = seaFloor[i][j+1] if j < len(seaFloor[i])-1 else None
    height = seaFloor[i][j]
    print('height: ', height, 'top: ', top, 'bottom: ', bottom, 'left: ', left, 'right: ', right)
    if (height < top or top is None) and (height < bottom or bottom is None) and (height < left or left is None) and (height < right or right is None):
      print("Danger at:", i, j, height)
      danger += 1 + height
    
  
print(danger)
