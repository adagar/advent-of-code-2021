file = open('input.txt', 'r')
lines = file.readlines()
intLines = [int(i) for i in lines]

count = 0
temp = intLines[0] + intLines[1] + intLines[2]
lineCounter = 0;

print(intLines, temp)


for i in range(len(intLines) - 2):
    newMeasurement = intLines[i] + intLines[i + 1] + intLines[i + 2]
    print(temp, newMeasurement)
    if newMeasurement > temp:
        count += 1
        
    temp = newMeasurement
    
    
print(count)
