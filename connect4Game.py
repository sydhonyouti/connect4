# Main file for the game implementation
# Need to add pygame and numpy to use the user interaction for connect 4

# Global Variables
row = 6
col = 7
board = []
boardLabel = []
winner = False

# Board setup
def createBoard(row, col):
    for i in range(8):
        if i < row:
            board.append(["_ " * col])
        elif i < col:
            board.append(["^"] * col)
        else:
            for j in range(row):
                boardLabel.append(str(j + 1))
            board.append(boardLabel)

def printBoard(board):
    print("\n")
    for row in board:
        print(" ".join(row))
    print("\n")

createBoard(row,col)
printBoard(board)