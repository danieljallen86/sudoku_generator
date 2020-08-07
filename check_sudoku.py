# Author: Dan Allen
# Date: 
# Description: 


def get_sol_from_file(file):
    """
    Converts a .txt file of a sudoku puzzle and returns a list of lists
    :param file: file with the sudoku solution
    :return: the solution in the form of a matrix (list of lists)
    """
    sol = []

    return sol


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

            # there can only be one instance of val in the row column and section
            if b_row.count(val) != 1 or b_col.count(val) != 1 or section.count(val) != 1:
                return False

    return True


def main(file):
    sol = get_sol_from_file(file)

    if check_sudoku_sol(sol):
        print("You did it!")

    else:
        print("Keep Trying!")
