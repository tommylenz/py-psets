# tictactoe1.py
# Created by Thomas Lenz 23/11/2020

def main():
    gameboard = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def print_board(board):
    print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " ")
    print("---+---+---")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " ")
    print("---+---+---")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " ")

if __name__ == "__main__":
    print_board([[' ','o',' '],[' ','o','x'],['x','x',' ']])
