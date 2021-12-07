file = open('input.txt', 'r')
lines = file.readlines()

def cleanInput(input):
  calledNums = []
  boards = []
  newBoard = []
  
  print("==========================")
  print(input)
  print("==========================")
  for line in input:
    print(line)
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
        print("Board added")
        print(boards)
        newBoard = []
      else:
        # print("Row added", clean)
        newRow = filter(lambda num: num != '', cleanLine)
        newIntRow = []
        for intStr in newRow:
          newIntRow.append([int(intStr), False])
        newBoard.append(newIntRow)
        
  
  print("==========================")
  print("INPUT CLEANED")
  print(boards)
  
  print("==========================")
  
  return calledNums, boards[1:]

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
  return False
  
def getScore(board, finalCall):
  unmarked = 0
  #get total of unmarked
  for row in board:
    for square in row:
      if(square[1] == False):
        unmarked += square[0]
  return unmarked * finalCall
  
def printBoard(board):
  for row in board:
    print(row)
  print("\n")
  
calledNums, boards = cleanInput(lines)
for board in boards:
  print(board)

# winner = False

for call in calledNums:
  print("CALLING", call)
  winningBoards = []
  for board in boards:
    for row in board:
      for num in row:
        if(num[0] == call):
          num[1] = True
          winner = checkForWin(board)
          if(winner):
            print(call, "Got a winner, removing")
            printBoard(board)
            # boards.remove(board)
            winningBoards.append(board)
            print("Remaining boards:")
            for remainingBoard in boards:
              printBoard(remainingBoard) 
              
            if(len(boards) == 1):
              print("Got it!")#, boards)
              printBoard(boards[0])
              print(getScore(boards[0], call))
              quit()
    
            break
  for winningBoard in winningBoards:
    boards.remove(winningBoard)
  

  
