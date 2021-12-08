import sys
import math
fileName = sys.argv[1]

fileData = open(fileName, 'r')
startingCrabs = [int(x) for x in fileData.read().split(",")]
climbingCostRef = {}

def getTotalCost(arr, target):   
  def getClimbingCost(distance):
    if distance in climbingCostRef:
      return climbingCostRef[distance]
    else:
      totalClimbingCost = 0
      for i in range(distance + 1):
        totalClimbingCost += i
      climbingCostRef[distance] = totalClimbingCost        
    return totalClimbingCost
        
  total = 0
  for num in arr:
    total += getClimbingCost(abs(num - target))
  return total
    
minCost = -1
target = 0

for i in range(0, max(startingCrabs)):
  cost = getTotalCost(startingCrabs, i)
  if cost < minCost or minCost == -1:
    minCost = cost
    target = i

print(target, minCost)
