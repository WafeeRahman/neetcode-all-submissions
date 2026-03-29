#Given an MXN matrix, if an element is zero, set its entire row and column to zeros
#Follow Up, solve in O(1 Space)

#The non O-1 solution would be to maintain a set of rows and columns such that each row and column are rows
#and cols that contain a zero, use two passes to set the matrix in place
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowSet = set()
        colSet = set() 

        ROWS, COLS = len(matrix), len(matrix[0])
        #Naive Solution, now lets try doing it at O(1) space
        #For each row and column that contain a zero, lets set the previous bordering cells as zeros
        #Edge Case, if we set the top border or bottom border to zero, how do we know that it should be zero?
        #We can use a flag when we set everything to zero
        """
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rowSet.add(r)
                    colSet.add(c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if r in rowSet or c in colSet:
                    matrix[r][c] = 0
        """
        
        firstRowZero = False
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    #If we encoutner a zero in the first row, set the flag to true
                    if r == 0:
                        print(matrix[r][c])
                        firstRowZero = True
                    else:
                        #Set markers for column and row to be zeroed out
                        matrix[r][0] = 0
                        matrix[0][c] = 0
        print(firstRowZero)
        #Iterate backwards and fill every
        for r in range(ROWS-1,-1,-1):
            for c in range(COLS-1,-1,-1):
                #If there was zero in the first row originally and we're in the first row
                #Zero it
                if r==0 and firstRowZero:
                    matrix[r][c] = 0
                    continue
                else:
                    if matrix[r][0] == 0 and r!=0:
                        matrix[r][c] = 0
                    elif matrix[0][c] == 0 and r!=0:
                        matrix[r][c] = 0
        

                    