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
