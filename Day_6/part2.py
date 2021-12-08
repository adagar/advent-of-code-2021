import sys
fileName = sys.argv[1]
days = int(sys.argv[2])

fileData = open(fileName, 'r')
startingFish = [int(x) for x in fileData.read().split(",")]


def sumFish(fishDict):
  totalFish = 0
  
  for key in fishDict:
    totalFish += fishDict[key]
    
  return totalFish
  
def consolidateFish(fishArr):
  fishDict = {}
  for fish in fishArr:
    if(fish in fishDict):
      fishDict[fish] += 1
    else:
      fishDict[fish] = 1
  return fishDict

fishDict = consolidateFish(startingFish)
    
for i in range(1, days + 1):
  print("After %i Days " % i)
  newFishDict = {} 
  for horninessRating in fishDict:
    if(horninessRating == 0):
      print(str(fishDict[horninessRating]) + " reproducing")
      newFishDict[8] = fishDict[horninessRating]
      newFishDict[6] = fishDict[horninessRating]
    else:
      if((horninessRating - 1) in newFishDict):
        newFishDict[horninessRating - 1] = fishDict[horninessRating] + newFishDict[horninessRating - 1]
      else:
        newFishDict[horninessRating-1] = fishDict[horninessRating]        
  fishDict = newFishDict
  print(fishDict)
  print("Total Fish: %i" % sumFish(fishDict))
  print("\n")
  

  6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8
    
print(fileName, days, startingFish, sumFish(fishDict))
print(consolidateFish([6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8]))
