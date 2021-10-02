# %%
# pip install numpy
import numpy as np

def create_board():
    board = np.zeros((6, 7))
    return board

def drop_piece():
    pass

def is_valid_location(board, col):
    return board[5][col] == 0

def get_next_open_row():
    pass

board = create_board()
game_over = False # True = someone wins (4 in a row)
turn = 0 # 0 - p1 turn

# %%
while not game_over:
    # Ask for Player 1 input
    if turn == 0:
        col = int(input("Player 1 make your selection (0-6):"))
        

    # Ask for Player 2 input
    else:
        col = int(input("Player 2 make your selection (0-6):"))

    turn += 1
    turn = turn % 2


# %%
