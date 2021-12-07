import sys
fileName = sys.argv[1]
days = int(sys.argv[2])

fileData = open(fileName, 'r')
startingFish = [int(x) for x in fileData.read().split(",")]

def breedFish(fishList):
    newFish = []
    for fish in fishList:
      fish -= 1
      if(fish < 0):
        newFish.append(8)
        newFish.append(6)
      else:
        newFish.append(fish)
    
    return newFish
    
for i in range(days):
  startingFish = breedFish(startingFish)
  # print(startingFish)
  
print(fileName, days, len(startingFish))
