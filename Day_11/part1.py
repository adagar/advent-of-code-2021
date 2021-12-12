import sys
from termcolor import colored
import os
import time

clear = lambda: os.system('clear')
fileName = sys.argv[1]
steps = 0
flashes = 0

def parseMyInput(file):
  fileData = open(file, "r")
  lines = fileData.readlines()
  rows = []
  for line in lines:    
    rows.append([int(char) for char in line.strip()])
    
  return rows

def printOctopi(octopi):
  time.sleep(0.05)
  # clear()
  for row in octopi:
    rowStr = ""
    for octo in row:
      if octo == 0:
        rowStr += colored(str(octo), 'green', attrs=['bold'])
      else:
        rowStr += str(octo)
        
      rowStr += " "
    print(rowStr)
  # clear()

def stepLocal(octopi, loc):
  # newFlashes = False
  (x, y) = loc
  surrounding = [(x-1, y-1), 
                 (x, y-1), 
                 (x+1, y-1), 
                 (x-1, y), 
                 (x+1, y), 
                 (x-1, y+1), 
                 (x, y+1), 
                 (x+1, y+1)]
  for neighbor in surrounding:    
    if neighbor[0] >= 0 and neighbor[0] < len(octopi) and neighbor[1] >= 0 and neighbor[1] < len(octopi[0]):
      if octopi[neighbor[0]][neighbor[1]] < 10 and octopi[neighbor[0]][neighbor[1]] != 0:
        octopi[neighbor[0]][neighbor[1]] += 1
        # if octopi[neighbor[0]][neighbor[1]] > 9:
        #   # newFlashes = True
          
  # return newFlashes
        

octopi = parseMyInput(fileName)

printOctopi(octopi)
print(octopi, len(octopi), len(octopi[0]))
while True:
  # Each octopus energy level increases by one
  for i in range(len(octopi)):
    for j in range(len(octopi[i])):
      octopi[i][j] = octopi[i][j] + 1
  
  
  while True:
    newFlashes = False
    for x in range(len(octopi)):
      for y in range(len(octopi[x])):
        # print(x, y, octopi[x][y], (octopi[x][y] > 9))
        if octopi[x][y] > 9:
          octopi[x][y] = 0
          flashes += 1
          stepLocal(octopi, (x, y))
          x = 0
          y = 0
          newFlashes = True
    if newFlashes is False:
      break
    # printOctopi(octopi)
    # break
     
  steps += 1
  nonFlashes = False
  
  for row in octopi:
    for octo in row:
      if octo != 0:
        nonFlashes = True
        
  if nonFlashes is False:
    break
  print("STEP", steps)
  printOctopi(octopi)
    
# printOctopi(octopi, flashes)
print(steps)
# clear()
