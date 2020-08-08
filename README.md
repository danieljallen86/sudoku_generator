# cs325_portfolio_project
## Contents
<ul>
<li><strong>README.md</strong></li>
<li><strong>sudoku.py</strong> - Generates a 9x9 sudoku board and solution</li>
<li><strong>check_sudoku.py</strong> - checks a sudoku solution for correctness</li>
<li><strong>test_sudoku.py</strong> - unittests for <code>sudoku.py</code> and <code>check_sudoku.py</code></li>
</ul>

## Instructions
###sudoku.py
Takes 0-1 arguments at the command line. User may indicate a desired difficulty scale from 1 (easy) - 5 (evil). 
The default is 3 if no entry or an invalid entry is passed.<br><br>

To run <code>sudoku.py</code>, enter the following a the command line:<br><br>
<code>python3 sudoku.py <i>difficulty</i></code> <br><br>
Where <code><i>difficulty</i></code> is an (optional) integer between 1 and 5.

###check_sudoku.py
Takes 1 argument at the command line. User provides the file name for the document containing their 
sudoku solution.


To run <code>check_sudoku.py</code>, enter the following a the command line:<br><br>
<code>python3 check_sudoku.py <i>file</i></code> <br><br>
Where <code><i>file</i></code> is an string of the file name.
