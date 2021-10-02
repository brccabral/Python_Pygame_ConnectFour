# %%
# pip install numpy
import numpy as np

def create_board():
    board = np.zeros((6, 7))
    return board

board = create_board()
game_over = False # True = someone wins (4 in a row)
turn = 0 # 0 - p1 turn

while not game_over:
    # Ask for Player 1 input
    if turn == 0:
        selection = int(input("Player 1 make your selection (0-6):"))
        print(selection)
        print(type(selection))
        break

    # Ask for Player 2 input

# %%
