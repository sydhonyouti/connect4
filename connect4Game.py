# Main file for the game implementation
# Need to add pygame and numpy to use the user interaction for connect 4

# Global Variables
import math
from random import random

row = 6
col = 7
board = []
boardLabel = []
winner = False

AI = 0  # representing as False
Player = 1  # representing as True

Player_Piece = 1
AI_Piece = 2


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

# Check if next row in selected column is open.
def openRow(board, col):
    for i in range(row):
        if board[i][col] == 0:
            return i

# Putting board pieces down
# Player is X and AI is 0
def dropPiece(board, row, col, piece):
    board[row][col] = piece


# Alpha Beta Pruning
# board = the board array
# depth = how deep we are trying to get into the tree
# alpha = - infinity
# beta = infinity
# maximizingPlayer = True for Player and False for AI

#get_valid_locations = this gets
def alphabeta(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = col_peek(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if check_win(board, AI_Piece):
                return (None, 100000000000000)
            elif check_win(board, Player_Piece):
                return (None, -10000000000000)
            else:  # Game is over, no more valid moves
                return (None, 0)
        else:  # Depth is zero
            return (None, score_position(board, AI_Piece))
    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = openRow(board, col)
            b_copy = board.copy()
            dropPiece(b_copy, row, col, AI_Piece)
            new_score = alphabeta(b_copy, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                print("Pruned")
                prune_score + 1
                break
        return column, value

    else:  # Minimizing player
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = openRow(board, col)
            b_copy = board.copy()
            dropPiece(b_copy, row, col, Player_Piece)
            new_score = alphabeta(b_copy, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                print("Pruned")
                prune_score + 1
                break
        return column, value

# Checking for a winning move
# player is whoever the turn is - could be Player or AI
def check_win(board, player):
    # check horizontal spaces
    for y in range(row):
        for x in range(col - 3):
            if board[x][y] == player and board[x+1][y] == player and board[x+2][y] == player and board[x+3][y] == player:
                return True

    # check vertical spaces
    for x in range(col):
        for y in range(row - 3):
            if board[x][y] == player and board[x][y+1] == player and board[x][y+2] == player and board[x][y+3] == player:
                return True

    # check diagonal spaces (/)
    for x in range(col - 3):
        for y in range(3, row):
            if board[x][y] == player and board[x+1][y-1] == player and board[x+2][y-2] == player and board[x+3][y-3] == player:
                return True

    # check diagonal spaces (\)
    for x in range(col - 3):
        for y in range(row - 3):
            if board[x][y] == player and board[x+1][y+1] == player and board[x+2][y+2] == player and board[x+3][y+3] == player:
                return True

    return False

# Loops through the game board to see what columns the AI can drop a piece in
def col_peek(board):
     valid_locations = []
     for boardCol in range(col):
         if inBound(board, col):
             valid_locations.append(col)
             return valid_locations

# Checks if its in bounds of the board
def inBound(board,col):
    return board[row - 1][col] == 0

# This function simulates dropping a piece
# We create a temporary board that will get passed in the scorePosition function
def simulateMove(board, piece):
    valid_location = col_peek(board)
    for col in valid_location:
        row = openRow(board, col)
        tempBoard = board.copy()  # Need this .copy() because when we use
                                  # numpy it will only copy the same memory location
        dropPiece(tempBoard, row, col, piece)
        score = scorePosition(tempBoard, piece)
        if score > bestScore:
            bestScore = score
            bestCol = col



# Player turn: Will be randomized
turn = random.randint(Player, AI)


createBoard(row,col)
printBoard(board)

# Main loop to start the game play
# It will keep going until there is a winner
while not winner:
    # Asking for Player input
    if turn == Player:
        playGame()
        winner = check_win(board, turn)
        turn += 1
        turn = turn % 2

        printBoard(board)
    # Asking for AI input
    if turn == AI and not winner:
        col, minmax

        #checking if this pushes something