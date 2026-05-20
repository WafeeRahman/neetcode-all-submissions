class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(r,c):
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or grid[r][c] == 0:
                return 0
            
            areaOfIsland = grid[r][c]
            grid[r][c] = 0
            areaOfIsland += dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

            return areaOfIsland
        
        res = -1
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, dfs(r,c))
        return res if res != -1 else 0

        