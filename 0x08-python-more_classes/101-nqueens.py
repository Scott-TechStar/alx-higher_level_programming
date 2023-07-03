#!/usr/bin/python3
""" A program that solves the N queens problem """

import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at board[row][col].
    """
    # Check the current column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the upper diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal
    i = row
    j = col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens_util(board, row, N, solutions):
    """
    A recursive utility function to solve the N-Queens problem.
    """
    if row == N:
        # All queens have been successfully placed, add the solution
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            # Place the queen at board[row][col]
            board[row][col] = 1

            # Recur to place the rest of the queens
            solve_nqueens_util(board, row + 1, N, solutions)

            # Backtrack and remove the queen from board[row][col]
            board[row][col] = 0


def solve_nqueens(N):
    """
    Solve the N-Queens problem and print all possible solutions.
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)

    for solution in solutions:
        print(solution)


if __name__ == '__main__':
    # Get the value of N from command line argument
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
