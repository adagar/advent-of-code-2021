file = open('input.txt', 'r')
lines = file.readlines()

def cleanInput(input):
  calledNums = []
  boards = []
  newBoard = []
  
  for line in input:
    if(len(calledNums) == 0):
      cleanLine = line[:-1].split(",") 
      # print(line[:-1].split(","))
      for call in cleanLine:
        calledNums.append(int(call))
    else:
      cleanLine = line[:-1].split(" ") 
      # print(cleanLine)
      if(cleanLine == ['']):
        boards.append(newBoard)
        newBoard = []
      else:
        newRow = filter(lambda num: num != '', cleanLine)
        newIntRow = []
        for intStr in newRow:
          newIntRow.append([int(intStr), False])
        newBoard.append(newIntRow)
        
  return calledNums, boards

def checkForWin(board):
  #check rows
  for row in board:
    count = 0
    for square in row:
      if(square[1] == True):
        count += 1
    if(count == len(row)):
      return True
  #check columns
  for i in range(len(board[0])):
    count = 0
    for row in board:
      if(row[i][1] == True):
        count += 1
    if(count == len(board)):
      return True
  #check diagonal down
  count = 0
  for i in range(len(board)):
    if(board[i][i][1] == True):
      count += 1
  if count == len(board):
    return True
    
  #check diagonal up
  count = 0
  for i in range(len(board)):
    if(board[i][len(board) - i - 1] == True):
      count += 1
  if count == len(board):
    return True
    
  return False
  
def getScore(board, finalCall):
  unmarked = 0
  #get total of unmarked
  for row in board:
    for square in row:
      if(square[1] == False):
        unmarked += square[0]
  return unmarked * finalCall
  
calledNums, boards = cleanInput(lines)

winner = False

for call in calledNums:
  if winner == True:
    break
  for board in boards:
    for row in board:
      for num in row:
        if(num[0] == call):
          num[1] = True
          winner = checkForWin(board)
          if(winner):
            print("Winner! : " + str(getScore(board, call)))
            break
        if(winner):
          break
      if(winner):
        break
    if(winner):
      break
    else:
      print("No winners for " + str(call))

  
