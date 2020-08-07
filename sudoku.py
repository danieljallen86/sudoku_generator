# Author: Dan Allen
# Date: 
# Description: 


import random
import math


def make_grid():
    """
    :return: an empty grid for sudoku (list of lists)
    """
    grid = [[0 for _ in range(9)] for _ in range(9)]
    return grid


def puzzle_seed():
    """
    :return: a list of 9 distinct random ints between 1-9 (int)
    """
    seed = list(range(1, 10))
    random.shuffle(seed)

    return seed


def check_sudoku_sol(sol):
    """
    Checks if the sudoku board is correct
    :param sol: completed board (list of list)
    :return: if the solution is valid (bool)
    """
    # determine the size of the sections
    # side = int(math.sqrt(len(sol)))

    # check every spot on board
    for row in range(len(sol)):
        for column in range(len(sol[row])):
            val = sol[row][column]  # value to check
            # calculate the section
            i = (row // 3) * 3  # beginning row of section
            j = (column // 3) * 3  # beginning column of section
            section = sol[i][j:j + 3] + sol[i + 1][j:j + 3] + sol[i + 2][j:j + 3]

            b_row = sol[row]
            b_col = [x[column] for x in sol]
            section = sol[i][i:i + 3] + sol[i + 1][i:i + 3] + sol[i + 2][i:i + 3]

            # there can only be one instance of val in the row column and section
            if b_row.count(val) != 1 or b_col.count(val) != 1 or section.count(val) != 1:
                return False

    return True


def works_in_spot(grid, row, col, digit):
    """
    Checks if a value works in a given spot on the sudoku board
    :param digit: value to check (int)
    :param row: row of spot on grid (int)
    :param col: column of spot on grid (int)
    :param grid: partially filled sudoku board (list of lists)
    :return: whether the value works in the position (bool)
    """
    # get the row and column
    b_row = grid[row]
    b_col = [x[col] for x in grid]

    # calculate the section
    i = (row // 3) * 3  # beginning row of section
    j = (col // 3) * 3  # beginning column of section
    section = grid[i][j:j + 3] + grid[i + 1][j:j + 3] + grid[i + 2][j:j + 3]

    # if the value is not present in the row column or section yet, it is  valid
    return digit not in b_row and digit not in b_col and digit not in section


def make_sudoku_board(grid, seed, sudoku=None):
    """
    Fills a sudoku board with a completed solution
    :param grid: a partially filled board (list of lists)
    :param seed: possible values for each spot on the grid (list)
    :param sudoku: variable for the completed sudoku
    :return: completed sudoku board (list of lists)
    """
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                # shuffle seed
                random.shuffle(seed)
                for digit in seed:
                    # if a digit in works in a spot
                    if works_in_spot(grid, row, col, digit):
                        grid[row][col] = digit  # assign the digit to that spot
                        all_rows = grid[0] + grid[1] + grid[2] + grid[3] + grid[4] + \
                                   grid[5] + grid[6] + grid[7] + grid[8]
                        # if there are still open spots on the grid
                        if 0 in all_rows:
                            # go back through function
                            sudoku = make_sudoku_board(grid, seed, sudoku)
                            # if the function returns no solution, backtrack
                            if not sudoku:
                                grid[row][col] = 0

                        # if a solution is found, assign it to sudoku
                        elif not sudoku:
                            sudoku = grid

                return sudoku


def remove_spots(board, difficulty):
    """
    Given a sudoku solution, this will remove values to create a puzzle
    :param board: filled sudoku board
    :param difficulty: how hard the puzzle should be on a scale from 1 (easy) - 4 (expert)
    :return: a partially filled sudoku board (list of lists)
    """
    pass
