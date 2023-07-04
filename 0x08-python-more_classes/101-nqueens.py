#!/usr/bin/python3
# 101-nqueens.py
# John Mwadime
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys

def nqueens(N):
    def is_safe(board, row, col):
        # Check if the current position is attacked by any previous queens
        # Check horizontally
        for i in range(col):
            if board[row][i] == 'Q':
                return False
        # Check diagonally (upper-left)
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        # Check diagonally (lower-left)
        i, j = row, col
        while i < N and j >= 0:
            if board[i][j] == 'Q':
                return False
            i += 1
            j -= 1
        return True

    def solve_nqueens(board, col):
        if col >= N:
            # Solution found, print the board configuration
            for row in board:
                print(' '.join(row))
            print()
            return
        for row in range(N):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                solve_nqueens(board, col + 1)
                board[row][col] = '.'
    
    # Input validation
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board
    board = [['.' for _ in range(N)] for _ in range(N)]
    solve_nqueens(board, 0)

# Run the program
if __name__ == '__main__':
    nqueens(int(sys.argv[1]))
