# Author: Dan Allen
# Date: 8/7/2020
# Description: Generates a partially filled sudoku and solution


import random
import sys


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
    Fills a sudoku board with a completed solution (modeled from Ajinkya Sonawane's solution on Medium's Daily Python)
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
                        all_rows = grid[0] + grid[1] + grid[2] + grid[3] + \
                            grid[4] + grid[5] + grid[6] + grid[7] + grid[8]
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


def pick_empty_spots(difficulty):
    """
    Generate spots to remove from a filled sudoku board
    :param difficulty: how hard the puzzle should be on a scale from 1 (easy) - 5 (evil) (int)
    :return: a partially filled sudoku board (list of tuples)
    """
    levels = {1: 35, 2: random.randint(36, 46), 3: random.randint(47, 50),
              4: random.randint(50, 53), 5: random.randint(54, 64)}

    empty_spots = set()

    # randomly pick a spot within the range of the 9x9 sudoku
    while len(empty_spots) < levels[difficulty]:
        spot = (random.randint(0, 8), random.randint(0, 8))
        empty_spots.add(spot)

    empty_spots = list(empty_spots)

    return empty_spots


def make_blanks(sudoku, difficulty=3):
    """
    Removes spots from a filled sudoku for someone to work on
    :param sudoku: full sudoku board (list of lists)
    :param difficulty: How challenging the puzzle will be on a scale from 1 (easy) - 5 (evil) (int)
    :return: sudoku board with blanks
    """
    empty_spots = pick_empty_spots(difficulty)

    for spot in empty_spots:
        row, col = spot
        sudoku[row][col] = ' '

    return sudoku


def puz_to_file(file, sudoku):
    """
    Outputs a sudoku to a file of the passed name
    :param file: The name of the file to be written to or created (str)
    :param sudoku: a sudoku solution or partially completed board (list of lists)
    :return: None
    """
    with open(file, 'w') as fw:
        for i in range(9):
            if i % 3 == 0:
                fw.write('=' * 33)

            fw.write(f'\n|| {sudoku[i][0]}  {sudoku[i][1]}  {sudoku[i][2]} |'
                     f' {sudoku[i][3]}  {sudoku[i][4]}  {sudoku[i][5]} |'
                     f' {sudoku[i][6]}  {sudoku[i][7]}  {sudoku[i][8]} ||\n')
        fw.write('=' * 33)


def main(difficulty='3'):
    # check that difficulty is a number
    try:
        difficulty = int(difficulty)
    except ValueError:
        difficulty = 3

    # ensure difficulty is in range
    if difficulty < 0 or difficulty > 5:
        difficulty = 3

    # generate a sudoku instance
    grid = make_grid()
    seed = puzzle_seed()
    sudoku = make_sudoku_board(grid, seed)

    # output solution to a file
    puz_to_file('sudoku_sol.txt', sudoku)

    # make a puzzle with blanks
    thinned_sudoku = make_blanks(sudoku, difficulty)
    # output puzzle to file
    puz_to_file('sudoku.txt', thinned_sudoku)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])

    else:
        main()
