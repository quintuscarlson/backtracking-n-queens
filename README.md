# Backtracking Constraint Solver (N-Queens)
A Python implementation of the classic N-Queens problem using recursive backtracking. The algorithm places one queen per column on an 8×8 chessboard while ensuring no two queens attack each other horizontally, vertically, or diagonally.

## Features 
- Recursive backtracking algorithm
- Checks rows, columns, and all diagonals for conflicts
- Prunes invalid board states early
- Console-based board visualization

## Usage 
from n_queens_solver import ChessBoard  
  
*# Initialize the chessboard*  
board = ChessBoard()  
  
*# Solve the 8-Queens problem*  
board.solve(0, 8)  
  
*# Print the final board configuration*  
board.printBoard()  

## How it Works
1. **Backtracking:** Place queens one column at a time.  
2. **Safety check:** Before placing, ensure no conflicts in the row, column, or diagonals.  
3. **Recursion:** Move to the next column if the current placement is valid.  
4. **Backtrack:** If no valid placement exists in a column, remove the previous queen and try the next row.  

## Board Representation 
`0` = empty square  
`1` = queen  
Example 8×8 board after solving:  
```
1  0  0  0  0  0  0  0   
0  0  0  0  0  0  1  0   
0  0  0  0  1  0  0  0   
0  0  0  0  0  0  0  1   
0  1  0  0  0  0  0  0   
0  0  0  1  0  0  0  0   
0  0  0  0  0  1  0  0   
0  0  1  0  0  0  0  0
``` 

## Requirements 
- Python 3.x

## Liscense
This project is open source and available under the MIT License.
