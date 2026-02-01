class chessBoard:

##class definition, create a 8x8 list of 0s to begin
    def __init__(self):
        self.boardLayout = [[0 for _ in range(8)] for _ in range(8)]

##function to print the contents of the chess boardLayout to the console
    def printBoard(self):
        for i in range(len(self.boardLayout)):
            print()
            for j in range(len(self.boardLayout)):
                print(self.boardLayout[i][j], end=" ")

##function to check if a certain square is safe from queens on the board               
    def isSafe(self, row, column):
        check = True

##check the current row
        for i in range(len(self.boardLayout)):
            if self.boardLayout[row][i] == 1:
                check = False

##check the current column
        for j in range(len(self.boardLayout[row])):
            if self.boardLayout[j][column] == 1:
                check = False

##check all 4 diagonals 
        for k in range(1, len(self.boardLayout)):
            if row-k >= 0 and column-k >= 0:
                if self.boardLayout[row-k][column-k] == 1:
                    check = False
            if row+k <= 7 and column-k >= 0:
                if self.boardLayout[row+k][column-k] == 1:
                    check = False
            if row-k >= 0 and column+k <= 7:
                if self.boardLayout[row-k][column+k] == 1:
                    check = False
            if row+k <= 7 and column+k <= 7:
                if self.boardLayout[row+k][column+k] == 1:
                    check = False

        return check


##recurive solve function
    def solve(self, column, n):

        ##end function if n is out of the range of possible solutions
        if not 0 <= n <= 8:
            return False

        ##end recursion if column is equal to 8 meaning every column has a queen in it
        if column == n:
                return True

        ##loop through each row in the paramter column   
        for row in range(len(self.boardLayout)):

            ##check if the current row & column are a safe place to put a queen and if so place one there
            if self.isSafe(row, column):
                self.boardLayout[row][column] = 1
                ##next check recursively if you can place a queen in the next column, if not undo the queen you placed in this iteration of the forloop by setting the position back to zero
                if self.solve(column + 1, n):
                    return True
                self.boardLayout[row][column] = 0
               
                
        return False
            


##main function to test the code
test = chessBoard()

test.printBoard()

test.solve(0, 8)
print()

test.printBoard()

