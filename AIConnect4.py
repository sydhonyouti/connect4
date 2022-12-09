import numpy as createBoard
import random
import math

maxRow = 6
maxCol = 7

HUMAN = 0
AI = 1

#EMPTY = 0
PLAYER_PIECE = 1
AI_PIECE = 2


def newBoard():
    board = createBoard.zeros((maxRow, maxCol))
    return board


def putPieceonBoard(board, row, col, piece):
    board[row][col] = piece

# Checks to see if the location is open to potentially drop a piece in
def locationExists(board, col):
    return board[maxRow - 1][col] == 0

# Check if next row in selected column is open.
def openRow(board, col):
    for r in range(maxRow):
        if board[r][col] == 0:
            return r


def printBoard(board):
    print(createBoard.flip(board, 0))

# Checking for a winning move
# player is whoever the turn is - could be Player or AI
def checkWin(board, piece):
    # Check horizontal locations for win
    for c in range(maxCol - 3):
        for r in range(maxRow):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(maxCol):
        for r in range(maxRow - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
                return True

    # Checks for positively sloped diagonals
    for c in range(maxCol - 3):
        for r in range(maxRow - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                return True

    # Checks for negatively sloped diagonals
    for c in range(maxCol - 3):
        for r in range(3, maxRow):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece:
                return True
def getExistingLoc(board):
    existingLoc = []
    for col in range(maxCol):
        if locationExists(board, col):
            existingLoc.append(col)
    return existingLoc

# There is 3 conditions that needs to be used
# 1. If Player wins
# 2. If AI wins
# 3. If the board is filled up
def terminalNode(board):
    return checkWin(board, PLAYER_PIECE) or checkWin(board, AI_PIECE) or len(getExistingLoc(board)) == 0

# Alpha Beta Pruning
# board = the board array
# depth = how deep we are trying to get into the tree
# alpha = - infinity
# beta = infinity
# maximizingPlayer = True for Player and False for AI
def alphabeta(board, depth, alpha, beta, maximizingPlayer):
    validLoc = getExistingLoc(board)
    terminal = terminalNode(board)
    if depth == 0 or terminal:
        if terminal:
            if checkWin(board, AI_PIECE):
                return (None, 100000000000)
            elif checkWin(board, PLAYER_PIECE):
                return (None, -10000000000)
            else:  # Game is over, no more valid moves
                return (None, 0)
        else:  # Depth is zero
            return (None, 0)
    if maximizingPlayer:
        value = -math.inf
        column = random.choice(validLoc)
        for col in validLoc:
            row = openRow(board, col)
            b_copy = board.copy()
            putPieceonBoard(b_copy, row, col, AI_PIECE)
            newScore = alphabeta(b_copy, depth - 1, alpha, beta, False)[1]
            if newScore > value:
                value = newScore
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:  # Minimizing player
        value = math.inf
        column = random.choice(validLoc)
        for col in validLoc:
            row = openRow(board, col)
            b_copy = board.copy()
            putPieceonBoard(b_copy, row, col, PLAYER_PIECE)
            newScore = alphabeta(b_copy, depth - 1, alpha, beta, True)[1]
            if newScore < value:
                value = newScore
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value

board = newBoard()
printBoard(board)
gameOver = False
turn = 0

while gameOver is False:
     # Ask for input
     if turn == 0:
          col = int(input("Your turn! Select a column between 0 - 6\n"))

          if locationExists(board, col):
               row = openRow(board, col)
               putPieceonBoard(board, row, col, 1)

               if checkWin(board, 1):
                    print("You Win!")
                    gameOver = True
     # Asks for AI input
     else:
         # col = int(input("Your turn Player 2, select a column 0 - 6"))
          col, minimax_score = alphabeta(board, 5, -math.inf, math.inf, True)
          if locationExists(board, col):
               row = openRow(board, col)
               putPieceonBoard(board, row, col, 2)

               if checkWin(board, 2):
                    print("AI wins")
                    gameOver = True

     printBoard(board)

     turn += 1
     turn = turn % 2