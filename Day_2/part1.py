file = open('input.txt', 'r')
lines = file.readlines()

horiz = 0
depth = 0

parsed_lines = []
for line in lines:
  newLine = line.split(' ')
  newDir = newLine[0]
  newMag = int(newLine[1])
  print(newDir, newMag)
  
  if newDir == "forward":
    horiz += newMag
  elif newDir == "up":
    depth -= newMag
  elif newDir == "down":
    depth += newMag
  else:
    print("Error")
    
print(horiz * depth)
  
  
