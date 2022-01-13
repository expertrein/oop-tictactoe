#Declare a global variable 
board = ["-", "-", "-",
         "-", "-", "-", 
         "-", "-", "-"]

currentPlayer = "X"
winner = None
gameRunning = True

#printing the game board (Prints the board without vlues but with gaps for the numbers indexed on the list from the first index to the ninth)

def printBoard(board):
    print(board[0]  + "|" +  board[1]  + "|" +  board[2])
    print("-----")
    print(board[3]  + "|" +  board[4]  + "|" +  board[5])
    print("-----")
    print(board[6]  + "|" +  board[7]  + "|" +  board[8])

#Take player input 

def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops player is already in that spot!")

#check for win or tie 

#check horizontaly
def checkHorizontle(board):
    global winner
    
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    global winner 
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

#check diagonal 

def checkDiag(board):
    global winner 
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True



#check for win or tie again

while gameRunning:
    printBoard(board)
    playerInput(board) 


