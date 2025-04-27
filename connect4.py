print("Welcome to Connect 4!")
#Collect Player Names
p1Name=str(input("Player 1, what is your name?\n"))
p2Name=str(input("Player 2, what is your name?\n"))
connect4table=[\
  [".",".",".",".",".","."],\
  [".",".",".",".",".","."],\
  [".",".",".",".",".","."],\
  [".",".",".",".",".","."],\
  [".",".",".",".",".","."],\
  [".",".",".",".",".","."],\
  [".",".",".",".",".","."]]

maxrow=6
maxcol=7

while True:
  #ask if players need help learning how to play connect 4
  explain_rules=str(input("Hi, "+p1Name+" and "+p2Name+", do you need any help before you start the game?\n"))  
  explain_rules=explain_rules.lower()
  if explain_rules=="yes" or explain_rules=="y":
    print("Here are the rules:\nTo win Connect Four, all you have to do is connect four of your colored checker pieces in a row, much the same as tic tac toe. This can be done horizontally, vertically or diagonally. Each player will drop in one checker piece at a time. This will give you a chance to either build your row, or stop your opponent from getting four in a row.\nGreat! Now that you understand the rules, let's start the game.")
    break
  elif explain_rules=="no" or explain_rules=="n":
    print("Great! Let's start the game!")
    break
  else:
    print("Please answer with a yes or no.")
  

def print_board(connect4table):
  '''Takes one input, connect4table, which is the who connect 4 board as sublists, and prints it'''
  finishedTable=""
  for row in range(maxrow):
    completedrow = ""
    for column in range(maxcol):
      itemInRow=str(connect4table[column][row])
      completedrow=completedrow+str(itemInRow)+"\t"
    finishedTable+=str(completedrow)+"\n"
  return finishedTable

def find_available_row(column,connect4table):
  '''Takes a single input,"collumn_num", and finds the first avalible space in the collumn to place a token'''
  for row in range(maxrow-1,-1,-1):
    print("checking ", row)
    hole=connect4table[column][row]
    if hole!="X" and hole!="O":#cannot place a token here
      return row
  return -1

def update_board(player,column,connect4table):
  '''updates the connect 4 board to include a player's move.'''
  row=find_available_row(column,connect4table)
  if row >= 0:
    print("Dropping token into row",str(row))
    connect4table[column][row]=player
  return connect4table

def check_connect_four(table,row,column,token):
  count=1
  for x in [1,-1]:# vertically 
    for i in range(x,4*x,x):
      if row+i in range(0,maxrow):
        if table[column][row+i]==token:
          # print("vertical", column, row, i)
          count+=1
      else:
        break
    if count>=4:
      return True
  count=1
  for y in [1,-1]:# horizontally
    for i in range(y,4*y,y):
      if column+i in range(0,maxcol):
        if table[column+i][row]==token:
          # print("horizontal", column, row, i)
          count+=1
      else:
        break
      if count>= 4:
        return True
  
  count=1
  for x in [1,-1]:#vertically(direction 1)
    for i in range(x,4*x,x):
      if column+i in range(0,maxcol) and row+i in range(0,maxrow): 
        if table[column+i][row+i]==token:
          # print("diag1", column, row, i, table[column+i][row+i])
          count+=1
      else:
        # print("diag1", column, row, i, table[column+i][row+i])
        break
    if count>=4:
      return True

  count=1
  for x in [1,-1]:#vertically(direction 2)
    for i in range(x,4*x,x):
      if column+i in range(0,maxcol) and row-i in range(0,maxrow):
        if table[column+i][row-i]==token:
          # print("diag2", column, row, i,table[column+i][row-i])
          count+=1
      else:
        # print("diag2", column, row, i, table[column+i][row-i])
        break
    if count>=4:
      return True
  return False

#---------------------start of game-----------------------
print("0\t1\t2\t3\t4\t5\t6\t")
print(print_board(connect4table))
num_of_turns=0
while True:
  if num_of_turns%2==0:
    PlayerName=p1Name
    PlayerIdentifier="X"
  else:
    PlayerName=p2Name
    PlayerIdentifier="O"
  while True:
    columnNum=input(PlayerName+", you're "+PlayerIdentifier+". What column do you want to play in?\t")
    possColumn=['0','1','2','3','4','5','6']
    if columnNum in possColumn:
      columnNum=int(columnNum)
      break
    else:
      print("Please enter a number between 0 and 6.")
 
  connect4table=update_board(PlayerIdentifier,columnNum,connect4table)
  connect4tableToPrint=print_board(connect4table)
  num_of_turns+=1
  
  row=find_available_row(columnNum,connect4table)+1
  print("row ", row)
  print("checking row %d column %d"%(row,columnNum))
  if check_connect_four(connect4table,row,columnNum,PlayerIdentifier):
    print("Horay!!!!")
    print(PlayerName + " is the winner!")
    print("This game took "+str(num_of_turns)+" turns.")
    print("\n0\t1\t2\t3\t4\t5\t6\t")
    print(connect4tableToPrint)
    break

  print("\n0\t1\t2\t3\t4\t5\t6\t")
  print(connect4tableToPrint)
  
#User tries to add to a full column
