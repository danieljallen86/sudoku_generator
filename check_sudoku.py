# Author: Dan Allen
# Date: 8/7/2020
# Description: Checks a sudoku instance for correctness


import re
import sys


def get_sol_from_file(file):
    """
    Converts a .txt file of a sudoku puzzle and returns a list of lists
    :param file: file with the sudoku solution
    :return: the solution in the form of a matrix (list of lists)
    """
    sol = []
    with open(file, 'r') as fr:
        for line in fr:
            row = re.findall('[0-9]+', line)
            sol.append(row)

    sol = sol[1::2]
    return sol


def check_sudoku_sol(sol):
    """
    Checks if the sudoku board is correct
    :param sol: completed board (list of list)
    :return: if the solution is valid (bool)
    """
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

            # there can only be one instance of val in the row column and section
            if b_row.count(val) != 1 or b_col.count(val) != 1 or section.count(val) != 1:
                return False

    return True


def main(file):
    sol = get_sol_from_file(file)

    if check_sudoku_sol(sol):
        print("\nYou did it!\n")

    else:
        print("\nKeep Trying!\n")


if __name__ == '__main__':
    main(sys.argv[1])
