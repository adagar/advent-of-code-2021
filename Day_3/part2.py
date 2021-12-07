file = open('input.txt', 'r')
lines = file.readlines()

def getOxyRating(arr, index = 0):
  zeroes = []
  ones = []
  if(len(arr) == 1):
    return arr[0][:-1]
  
  for y in range(len(arr)):
    if(arr[y][index] == '0'):
      zeroes.append(arr[y])
    else:
      ones.append(arr[y])
      
  if(len(zeroes) <= len(ones)):
    return getOxyRating(zeroes, index + 1)
  else:
    return getOxyRating(ones, index + 1)
      
def getCO2Rating(arr, index = 0):
  zeroes = []
  ones = []
  if(len(arr) == 1):
    return arr[0][:-1]
  
  for y in range(len(arr)):
    if(arr[y][index] == '0'):
      zeroes.append(arr[y])
    else:
      ones.append(arr[y])
      
  if(len(zeroes) > len(ones)):
    return getCO2Rating(zeroes, index + 1)
  else:
    return getCO2Rating(ones, index + 1)
      
def convArrToInt(arr):
  return int(''.join(arr), 2)
  
splitLines = [list(line) for line in lines]

oxyRate = getOxyRating(splitLines)
co2Rate = getCO2Rating(splitLines)


      
    

print(convArrToInt(oxyRate) * convArrToInt(co2Rate))
