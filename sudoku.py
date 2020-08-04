# Author: Dan Allen
# Date: 
# Description: 


# code starts here
def check_sudoku_sol(matrix):
    """
    Checks if the sudoku board is correct
    :param matrix: completed board (list of list)
    :return: if the solution is valid (bool)
    """
    # check every spot on board
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            val = matrix[row][column]
            i = (row // 3)*3
            b_row = matrix[row]
            b_col = [x[0] for x in matrix]
            section = matrix[i][i:i + 3] + matrix[i + 1][i:i + 3] + matrix[i + 2][i:i + 3]

            if b_row.count(val) != 1 or b_col.count(val) != 1 or section.count(val) != 1:
                return False

    return True

# row_j = board[j]
# column_i = [x[0] for x in board]
# r = i // 3
# section = matrix[r][r:r+3]+matrix[r+1][r:r+3]+matrix[r+2][r:r+3]
