class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        atlSet = set()
        pacSet = set()
        grid = heights
        def dfs(r,c,prevDepth,visit):
            if r>=ROWS or c>=COLS or r<0 or c<0 or prevDepth > grid[r][c] or (r,c) in visit:
                return
            
            visit.add((r,c))
            dfs(r+1,c,grid[r][c], visit)
            dfs(r,c-1,grid[r][c], visit)
            dfs(r,c+1,grid[r][c], visit)
            dfs(r-1,c,grid[r][c], visit)
        
        for c in range(COLS):
            dfs(0,c,-1,pacSet)
            dfs(ROWS-1, c,-1,atlSet)
        
        for r in range(ROWS):
            dfs(r,0,-1,pacSet)
            dfs(r,COLS-1,-1,atlSet)
        
        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atlSet and (r,c) in pacSet:
                    res.append([r,c])
        return res