class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}


        def dp(r,c, curCost):
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0:
                return float('inf')
            if r==len(grid)-1 and c == len(grid[0])-1:
                return curCost + grid[len(grid)-1][len(grid[0]) -1]
            if (r,c, curCost) in memo:
                return memo[(r,c, curCost)]
            
            for dr, dc in [[0,1], [1,0]]:
                memo[(r,c, curCost)] = min(memo.get((r,c, curCost), float('inf')), dp(r+dr, c+dc, curCost+grid[r][c]))
            
            return memo[(r,c, curCost)]
        return dp(0,0,0)
            