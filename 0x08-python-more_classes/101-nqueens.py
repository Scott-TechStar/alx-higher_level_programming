#!/usr/bin/python3
from sys import argv as arg

counter = len(arg)
N = 0
row = 0
columns = 0
chess = []

def nqueens(chess):

    if counter != arg:
        print("Usage: nqueens N")
        exit (1)

    if N < 4:
        print("N must be at least 4")
        exit (1)

    if type(N) is not int:
        print("N must be a number")

    for row in range(N):
        for columns in range(N):
            print(chess[row][columns])

def check_queen(chess):
    
