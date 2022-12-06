# Main file for the game implementation
# Need to add pygame and numpy to use the user interaction for connect 4

# Global Variables
row = 6
col = 7
board = []
boardLabel = []
winner = False
lastTurn = 0
AI = False
Player = True

# Board setup
def createBoard(row, col):
    for i in range(8):
        if i < row:
            board.append(["_ " * col])
        elif i < col:
            board.append(["^"] * col)
        else:
            for j in range(row + 1):
                boardLabel.append(str(j + 1))
            board.append(boardLabel)

def printBoard(board):
    print("\n")
    for row in board:
        print(" ".join(row))
    print("\n")


# Putting board pieces down
def dropPiece(lastTurn, col):
    if Player == True:
        board[lastTurn][col] = "X"
    else:
        board[lastTurn][col] = "O"
    printBoard(board)

# Keep the game to running (True) til it breaks. Then we can stop the game
def playGame():
    while True:
        try:
            column = int(input("Pick a column (1 - 7)")) - 1
            if column >= 1 and column <= col:
                for i in range(6):
                    if board[i][column] == "_":
                        last = i
                dropPiece(last, column)
            else:
                raise "ERROR: You picked a column outside the board"
            break
        except:
            print("Not a valid number! Please try again")

# Function to check for a player win

createBoard(row,col)
printBoard(board)
