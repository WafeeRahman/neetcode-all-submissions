class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.preSum = [[[0] for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        for i in range(len(self.matrix)):
            prefix = 0
            for j in range(len(self.matrix[i])):
                prefix += self.matrix[i][j]
                self.preSum[i][j] = prefix
                if i > 0:
                    self.preSum[i][j] += self.preSum[i-1][j]
        print(self.preSum)
        
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        bottomRight=self.preSum[row2][col2]
        left = self.preSum[row2][col1-1] if col1 > 0 else 0
        above = self.preSum[row1-1][col2] if row1 > 0 else 0
        overlap = self.preSum[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0

        return bottomRight - left - above + overlap

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)