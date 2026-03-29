class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        curArea = 0
        maxArea = 0

        def dfs(r, c, path):
            nonlocal curArea, grid
            
            if (min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0 or (r,c) in path):
                return 
        
            if grid[r][c] == 1:
                curArea += 1
                grid[r][c] = 0
            
            path.add((r,c))

            dfs(r+1, c, path)
            dfs(r-1, c, path)
            dfs(r, c+1, path)
            dfs(r, c-1, path)
            path.remove((r,c))
            
            return
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    dfs(row, col, set())
                    maxArea = max(curArea, maxArea)
                curArea = 0
        return maxArea

            


