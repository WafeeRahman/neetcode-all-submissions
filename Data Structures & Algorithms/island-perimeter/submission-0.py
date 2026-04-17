class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        perim = 0
        visit = set()
        def check(r,c):
            nonlocal perim
            if r >= ROWS or c >= COLS or c < 0 or r < 0 or (r,c) in visit:
                return False

            visit.add((r,c))
            if r+1 >= ROWS or grid[r+1][c] == 0:
                perim += 1
            if r-1 < 0 or grid[r-1][c] == 0:
                perim += 1
            if c+1 >= COLS or grid[r][c+1] == 0:
                perim+=1
            if c-1 < 0 or grid[r][c-1] == 0:
                perim += 1
            
   

            return True
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    check(r,c)
        return perim
