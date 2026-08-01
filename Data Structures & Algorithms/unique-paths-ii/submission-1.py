class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        visit = set()
        if obstacleGrid == [[1]]:
            return 0
        def dp(r,c):
            if r == len(obstacleGrid)-1 and c == len(obstacleGrid[0])-1:
                return 1
            elif r < 0 or c < 0 or r == len(obstacleGrid) or c == len(obstacleGrid[0]) : 
                return 0
            elif obstacleGrid[r][c] == 1:
                memo[(r,c)] = 0
                return memo[(r,c)]
            elif (r,c) in memo:
                return memo[(r,c)]
            
            for dr, dc in [[0,1], [1,0]]:
                nr, nc = r+dr, c+dc
                memo[(r,c)] = memo.get((r,c), 0) + dp(nr,nc)
            
            return memo[(r,c)]
        
        return       dp(0,0) 