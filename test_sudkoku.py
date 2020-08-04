# Author: Dan Allen
# Date: 
# Description: Unittest for ___.py


import unittest
from sudoku import check_sudoku_sol


class MyTestCase(unittest.TestCase):
    def test_check_sol(self):
        sb1 = [[8, 2, 7, 1, 5, 4, 3, 9, 6],
               [9, 6, 5, 3, 2, 7, 1, 4, 8],
               [3, 4, 1, 6, 8, 9, 7, 5, 2],
               [5, 9, 3, 4, 6, 8, 2, 7, 1],
               [4, 7, 2, 5, 1, 3, 6, 8, 9],
               [6, 1, 8, 9, 7, 2, 4, 3, 5],
               [7, 8, 6, 2, 3, 5, 9, 1, 4],
               [1, 5, 4, 7, 9, 6, 8, 2, 3],
               [2, 3, 9, 8, 4, 1, 5, 6, 7]]
        sb2 = [[6, 5, 7, 8, 1, 9, 3, 4, 2],
               [2, 8, 9, 7, 3, 4, 6, 5, 1],
               [4, 3, 1, 5, 2, 6, 9, 8, 7],
               [5, 8, 9, 1, 4, 7, 2, 6, 3],
               [7, 1, 2, 3, 6, 8, 4, 9, 5],
               [3, 6, 4, 2, 9, 5, 7, 1, 8],
               [9, 2, 3, 6, 8, 1, 5, 7, 4],
               [1, 4, 5, 9, 7, 3, 8, 2, 6],
               [8, 7, 6, 4, 5, 2, 1, 3, 9]]
        self.assertTrue(check_sudoku_sol(sb1))
        self.assertTrue(check_sudoku_sol(sb2))


if __name__ == '__main__':
    unittest.main()
