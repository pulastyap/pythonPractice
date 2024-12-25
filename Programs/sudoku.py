#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 08:32:56 2024

@author: pulastya
"""

def print_grid(grid):
    """
    Function to print the Sudoku grid in a readable format.
    """
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_safe(grid, row, col, num):
    """
    Check if placing 'num' at grid[row][col] is safe.
    """
    # Check the row
    if num in grid[row]:
        return False
    
    # Check the column
    if num in [grid[i][col] for i in range(9)]:
        return False
    
    # Check the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False
                
    return True

def solve_sudoku(grid):
    """
    Solve the Sudoku puzzle using backtracking.
    """
    # Find the next empty spot
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                # Try placing digits 1-9
                for num in range(1, 10):
                    if is_safe(grid, row, col, num):
                        grid[row][col] = num  # Place the number
                        
                        # Recursively attempt to solve the rest
                        if solve_sudoku(grid):
                            return True
                        
                        # Backtrack
                        grid[row][col] = 0
                
                # If no number fits, return False
                return False
                
    return True  # Return True if the grid is solved

# Example Sudoku puzzle (0 represents empty cells)
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Sudoku Puzzle:")
print_grid(sudoku_grid)

if solve_sudoku(sudoku_grid):
    print("\nSolved Sudoku:")
    print_grid(sudoku_grid)
else:
    print("\nNo solution exists.")
