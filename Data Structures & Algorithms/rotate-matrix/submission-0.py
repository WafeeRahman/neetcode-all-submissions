#Given a square matrix, move all rows and columns 90 degrees clockwise
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for r in range(n):
            for c in range(r, n):
                tmp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = tmp
        for r in range(n):
            matrix[r].reverse()
            