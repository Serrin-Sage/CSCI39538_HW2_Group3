#Serrin Doscher
#CSCI 39538
#Recreational Math Assignment

import numpy as np
"""
NxN square
Given an N, each tile in the grid contains a number.
Each row, column and diagonal add up to the same value.
"""

def magic_square_odd(N):
    magic_constant = N*((N**2 + 1)/2)
    grid = np.zeros((N, N), dtype=int)
    row_index = 0
    col_index = N//2
    n = 1
    N_sqrd = N**2
    while n <= N_sqrd:
        grid[row_index, col_index] = n
        n += 1
        new_row = (row_index - 1) % N
        new_col = (col_index + 1) % N

        if grid[new_row, new_col]:
            row_index += 1
        else:
            row_index = new_row
            col_index = new_col

    print(grid)
    print(f'The Magic Constant is {magic_constant}')

N = int(input("Enter size of Magic Square (greater than 2): "))

if N % 2 == 1:
    magic_square_odd(N)
if N % 2 == 0:
    print("NOT IMPLEMENTED")