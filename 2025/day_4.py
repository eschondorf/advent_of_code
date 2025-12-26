import util
import math
import time
import numpy as np

def create_grid(inpt):
    m = len(inpt)
    n = len(inpt[0])
    arr = np.zeros((m+2, n+2))
    for i, row in enumerate(inpt):            
        for j, elt in enumerate(row):
            if elt == '@':
                arr[i+1, j+1] = 1

    return arr

def remove_tp(grid):
    rv = 0
    for i, row in enumerate(grid):            
        for j, elt in enumerate(row):
            if elt == 1:
                neighbors = grid[i, j-1] + grid[i, j+1] + grid[i+1, j-1] + grid[i+1, j] + grid[i+1, j+1] + grid[i-1, j-1] + grid[i-1, j] + grid[i-1, j+1]
                if neighbors < 4: 
                    rv += 1
                    grid[i,j] = 0
    return rv, grid
    
                


def solver(inpt):
    rv1 = 0
    rv2 = 0
    grid = create_grid(inpt)
    #print(inpt)
    #print(grid)
    for i, row in enumerate(grid):            
        for j, elt in enumerate(row):
            if elt == 1:
                neighbors = grid[i, j-1] + grid[i, j+1] + grid[i+1, j-1] + grid[i+1, j] + grid[i+1, j+1] + grid[i-1, j-1] + grid[i-1, j] + grid[i-1, j+1]
                if neighbors < 4: rv1 += 1
    another_loop = True
    while another_loop:
        rv, grid = remove_tp(grid)
        rv2 += rv
        another_loop = (rv != 0)

    return rv1, rv2



if __name__ == "__main__":
    inpt = util.read_strs("inputs/day_4_input.txt", sep = "\n")
    tst = util.read_strs("inputs/day_4_test.txt", sep = "\n")

    print("TASK 1 and 2")
    util.call_and_print(solver, inpt)
    util.call_and_print(solver, tst)
