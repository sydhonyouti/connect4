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
#Check if next row in selected column is open
def openRow(board, col):
    for i in range(row):
        if board[i][col] == 0
            return i

# Putting board pieces down
# Player is X and AI is 0
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

# Alpha Beta Pruning
# board = the board array
# depth = how deep we are trying to get into the tree
# alpha = - infinity
# beta = infinity
# maximizingPlayer = True for Player and False for AI
def alphabeta(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, AI_PIECE):
                return (None, 100000000000000)
            elif winning_move(board, PLAYER_PIECE):
                return (None, -10000000000000)
            else:  # Game is over, no more valid moves
                return (None, 0)
        else:  # Depth is zero
            return (None, score_position(board, AI_PIECE))
    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, AI_PIECE)
            new_score = minimax(b_copy, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:  # Minimizing player
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            dropPiece(b_copy, row, col, PLAYER_PIECE)
            new_score = minimax(b_copy, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
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