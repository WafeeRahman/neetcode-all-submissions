#Our goal is to create a matrix where we can calculate the sumRegion at O(1) lookup
#We can do this w/ prefix sums, where we the ijth position of the matrix is the prefix of each row and col preceding
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.preMatrix = [[0] * (COLS + 1) for _ in range (ROWS+1)]

        for i in range(len(matrix)):
            prefix = 0
            for j in range(len(matrix[i])):
                prefix += matrix[i][j]
                above = self.preMatrix[i][j+1] #Above Prefix
                self.preMatrix[i+1][j+1] = prefix + above
                

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        row2 += 1
        col1 += 1
        col2 += 1

        bottomRight = self.preMatrix[row2][col2]
        above = self.preMatrix[row1-1][col2] #Eliminate everything above the square
        left = self.preMatrix[row2][col1-1] #Remove all left values from the square
        topLeft = self.preMatrix[row1-1][col1-1] #Add back topleft, as subtractive left and above removes topleft twice

        return bottomRight - above -left + topLeft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)