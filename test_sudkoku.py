# Author: Dan Allen
# Date: 8/7/2020
# Description: Unittest for sudoku.py and check_sudoku.py


import unittest
from sudoku import works_in_spot, make_sudoku_board, puzzle_seed, make_grid, puz_to_file, make_blanks
from check_sudoku import check_sudoku_sol, get_sol_from_file


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

        sb2 = [[3, 2, 7, 6, 8, 9, 1, 5, 4],
               [9, 6, 8, 5, 1, 4, 7, 3, 2],
               [5, 1, 4, 7, 2, 3, 6, 9, 8],
               [8, 4, 1, 9, 6, 5, 3, 2, 7],
               [6, 5, 3, 8, 7, 2, 9, 4, 1],
               [2, 7, 9, 4, 3, 1, 8, 6, 5],
               [7, 9, 2, 1, 5, 6, 4, 8, 3],
               [1, 3, 6, 2, 4, 8, 5, 7, 9],
               [4, 8, 5, 3, 9, 7, 2, 1, 6]]
        self.assertTrue(check_sudoku_sol(sb1))
        self.assertTrue(check_sudoku_sol(sb2))

    def test_spot_check(self):
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
        self.assertTrue(works_in_spot(sb1, 0, 0, 10))
        self.assertTrue(works_in_spot(sb2, 0, 0, 10))
        self.assertFalse(works_in_spot(sb1, 0, 0, 6))
        self.assertFalse(works_in_spot(sb2, 0, 0, 6))

    def test_board_gen(self):
        for _ in range(20):
            grid1 = make_grid()
            puz_seed = puzzle_seed()
            sudoku = make_sudoku_board(grid1, puz_seed)
            self.assertTrue(check_sudoku_sol(sudoku))

    def test_file_io(self):
        grid = make_grid()
        seed = puzzle_seed()
        sudoku = make_sudoku_board(grid, seed)
        puz_to_file('sudoku_sol.txt', sudoku)
        sudoku = make_blanks(sudoku)
        puz_to_file('sudoku.txt', sudoku)
        sol = get_sol_from_file('sudoku_sol.txt')
        self.assertTrue(check_sudoku_sol(sol))

    def test_rand_file_check(self):
        for _ in range(20):
            grid = make_grid()
            seed = puzzle_seed()
            sudoku = make_sudoku_board(grid, seed)
            puz_to_file('sudoku_sol.txt', sudoku)
            sol = get_sol_from_file('sudoku_sol.txt')
            self.assertTrue(check_sudoku_sol(sol))


if __name__ == '__main__':
    unittest.main()
