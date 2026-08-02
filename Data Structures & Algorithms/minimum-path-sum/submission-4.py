class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}


        def dp(r,c):
            if r >= len(grid) or c >= len(grid[0]):
                return float('inf')
            if r==len(grid)-1 and c == len(grid[0])-1:
                return grid[r][c]
            if (r,c) in memo:
                return memo[(r,c)]
            
            for dr, dc in [[0,1], [1,0]]:
                memo[(r,c)] = grid[r][c] + min(dp(r+1,c), dp(r, c+1))
            
            return memo[(r,c)]
        return dp(0,0)
            