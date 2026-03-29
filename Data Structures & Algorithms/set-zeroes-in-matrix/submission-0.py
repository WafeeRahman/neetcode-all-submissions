#Given an MXN matrix, if an element is zero, set its entire row and column to zeros
#Follow Up, solve in O(1 Space)

#The non O-1 solution would be to maintain a set of rows and columns such that each row and column are rows
#and cols that contain a zero, use two passes to set the matrix in place
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowSet = set()
        colSet = set() 

        ROWS, COLS = len(matrix), len(matrix[0])

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rowSet.add(r)
                    colSet.add(c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if r in rowSet or c in colSet:
                    matrix[r][c] = 0
    
        