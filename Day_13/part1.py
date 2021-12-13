import sys
 
fileName = sys.argv[1]

def parseMyFile(file):
  fileData = open(file, "r")
  lines = fileData.readlines()
  
  dots = []
  instructions = []
  
  active = dots
  for line in lines:
    if line == '\n':
      active = instructions
    else:
      if active == dots:
        active.append([int(char) for char in line.strip().split(',')])
      else:
        instructions.append([line.strip().split(' ')[2].split('=')[0],int(line.strip().split(' ')[2].split('=')[1])])
 
  return dots, instructions
    
def getDimensions(dots):
  maxX = maxY = 0
  for dot in dots:
    if dot[0] > maxX:
      maxX = dot[0]
    if dot[1] > maxY:
      maxY = dot[1]
  return maxX, maxY

def ySlice(paper, y):
  topHalf = []
  bottomHalf = []
  
  # print(paper)
  for row in range(0, y):
    topHalf.append(paper[row])
  for row in reversed(range(y + 1, len(paper))):
    bottomHalf.append(paper[row])
    
  # print (topHalf, bottomHalf)
  return topHalf, bottomHalf
  
def xSlice(paper, x):
  leftHalf = []
  rightHalf = []
  
  for row in paper:
    leftHalf.append(row[0:x ])
    rightHalf.append(row[x + 1::][::-1])
    
  
    
  # print (leftHalf, rightHalf)
  # for row in leftHalf:
  #   for char in row:
  #     print(char, end=' ')
  #   print()
    
  # print()
      
  # for row in rightHalf:
  #   for char in row:
  #     print(char, end=' ')
  #   print()
      
  return leftHalf, rightHalf
  
  
parseMyFile(fileName)
dots, instructions = parseMyFile(fileName)
dimensions = getDimensions(dots)
paper = []

# print(dots)
print(instructions)
# print(dimensions)

for y in range(dimensions[1] + 1):
  newRow = []
  for x in range(dimensions[0] + 1):
    if [x, y] in dots:
      newRow.append('#')
    else:
      newRow.append('.')
  paper.append(newRow)


# for row in paper:
#   for char in row:
#     print(char, end=' ')
    
#   print()


for instruction in instructions:
  count = 0
  print(instruction)
  if instruction[0] == 'y':
    topHalf, bottomHalf = ySlice(paper, instruction[1])
    # combine them
    newPaper = []
    for y in range(len(topHalf)):
      newRow = []
      for x in range(len(topHalf[y])):
        char = topHalf[y][x]
        if char == '#' or bottomHalf[y][x] == '#':
          newRow.append('#')
        else:
          newRow.append('.')
      newPaper.append(newRow)
    paper = newPaper
  elif instruction[0] == 'x':
    leftHalf, rightHalf = xSlice(paper, instruction[1])
    # combine them
    newPaper = []
    for y in range(len(leftHalf)):
      newRow = []
      for x in range(len(leftHalf[y])):
        char = leftHalf[y][x]
        if char == '#' or rightHalf[y][x] == '#':
          newRow.append('#')
        else:
          newRow.append('.')
      newPaper.append(newRow)
    paper = newPaper
  # count em
  for row in paper:
    for char in row:
      if char == '#':
        count += 1
  print(count)

  for row in paper:
    for char in row:
      print(char, end=' ')
      
    print()
