#!/usr/bin/python3
"""Solves N Queen Problem
"""


def print_queens(solutions=[]):
    """Prints the solutions

    Args:
        solutions (list): List of list of position of the queens
    """
    for board in solutions:
        print([[i, x] for i, x in enumerate(board)])


def is_safe(queens, row, column):
    """Checks if the queen can be placed in a position

    Args:
        queens (list): Chess board with queens positions
        row (int): row position
        column (int): column position

    Returns:
        True: if the queen can be placed at (row, column)
        False: If the queen can't be placed at (row, column)
    """
    for i in range(1, row + 1):
        # Check Column
        if queens[row - i] == column:
            return False

        # Check upleft diagonal
        if queens[row - i] == column - i:
            return False

        # Check upright diagonal
        if queens[row - i] == column + i:
            return False
    return True


def find_position(queens, k, N):
    """Find a safe column position for a queen

    Args:
        queens (list): N x N chess board with queens positions
        k (int): row position
        N (int): size of the chess board

    Returns:
        (int) Safe column if found else -1
    """
    for j in range(queens[k] + 1, N):
        if is_safe(queens, k, j):
            return j
    return -1


def solve_queens(queens, row=0, offset=-1):
    """Returns a single solution for N Queen given a start index
    for the first queen

    Args:
        N (int): size of the chess board
        start (int): initial column value for queen at row 0

    Return:
        (list): a solution
    """
    N = len(queens)
    queens = [-1 for i in range(N)]
    k = 0
    while k >= 0 and k < N:
        j = find_position(queens, k, offset)
        if j < 0:
            queens[k] = -1
            k -= 1
        else:
            queens[k] = j
            k += 1

    if k == -1:
        return None

    return queens


def nqueens(N):
    """Print every possible solution to the given N problem

    Args:
        N (int): size of chessboard
    """
    queens = [-1 for i in range(N)]
    solve_queens(queens)


if __name__ == "__main__":
    import sys

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

    nqueens(N)
