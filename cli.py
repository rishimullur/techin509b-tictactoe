# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board
from logic import get_winner
from logic import show_current_board
from logic import update_board
from logic import other_player

# Reminder to check all the tests

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    # Intiazlize the first move to X
    char = 'X'

    while winner == None:
        print("Begin Turn!")
        print("It's", char, "turn!")
        show_current_board(board=board)
        print("Enter the row and column of the board you want to add the move to:")
        i = int(input("Enter the row:"))
        j = int(input("Enter the column:"))
        board = update_board(board=board,i=i,j=j,char=char)
        char = other_player(player = char)
        winner = get_winner(board)

