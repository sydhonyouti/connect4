import numpy as np
import random
import math

ROW_COUNT = 6
COLCOUNT = 7

PLAYER = 0
AI = 1

EMPTY = 0
PLAYER_PIECE = 1
AI_PIECE = 2

prune = 0


def create_board():
    board = np.zeros((ROW_COUNT, COLCOUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLCOUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLCOUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
                return True

    # Check positively sloped diaganols
    for c in range(COLCOUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                return True

    # Check negatively sloped diaganols
    for c in range(COLCOUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece:
                return True
def get_valid_locations(board):
    valid_locations = []
    for col in range(COLCOUNT):
        if is_valid_location(board, col):
            valid_locations.append(col)
    return valid_locations

def is_terminal_node(board):
    return winning_move(board, PLAYER_PIECE) or winning_move(board, AI_PIECE) or len(get_valid_locations(board)) == 0

def alphabeta(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, AI_PIECE):
                return (None, 100000000000)
            elif winning_move(board, PLAYER_PIECE):
                return (None, -10000000000)
            else:  # Game is over, no more valid moves
                return (None, 0)
        else:  # Depth is zero
            return (None, 0)
    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, AI_PIECE)
            new_score = alphabeta(b_copy, depth - 1, alpha, beta, False)[1]
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
            drop_piece(b_copy, row, col, PLAYER_PIECE)
            new_score = alphabeta(b_copy, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value

board = create_board()
print_board(board)
gameOver = False
turn = 0

while gameOver is False:
     # Ask for Player 1 input
     if turn == 0:
          col = int(input("Your turn Player 1, select a column 0 - 6"))

          if is_valid_location(board, col):
               row = get_next_open_row(board, col)
               drop_piece(board, row, col, 1)

               if winning_move(board, 1):
                    print("Player 1 wins")
                    gameOver = True
     # Ask for Player 2 input
     else:
         # col = int(input("Your turn Player 2, select a column 0 - 6"))
          col, minimax_score = alphabeta(board, 5, -math.inf, math.inf, True)
          if is_valid_location(board, col):
               row = get_next_open_row(board, col)
               drop_piece(board, row, col, 2)

               if winning_move(board, 2):
                    print("Player 2 wins")
                    gameOver = True

     print_board(board)

     turn += 1
     turn = turn % 2
