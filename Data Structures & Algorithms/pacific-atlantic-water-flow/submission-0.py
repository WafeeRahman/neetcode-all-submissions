class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        ROWS, COLS = len(heights), len(heights[0])
        def dfs(heights, r, c, visit, target):
            nonlocal ROWS, COLS
            
            if (min(r, c) < 0 or r == ROWS or c == COLS or (r,c) in visit):
                return False

            visit.add((r,c))
            #Atlantic Ocean
            if r in target or c in target:
                return True
            
            dirs = [[1,0], [-1, 0], [0, 1], [0,-1]]
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if min(nr,nc) < 0 or nr == ROWS or nc == COLS:
                    continue
                if heights[r][c] >= heights[nr][nc]: 
                   if dfs(heights, nr, nc, visit, target):
                    return True

            return False
        
        for r in range(len(heights)):
            for c in range(len(heights[r])):
                if dfs(heights, r, c, set(), [0,0]) and dfs(heights,r,c,set(),[ROWS-1, COLS-1]):
                    res.append([r,c])
        return res

            


                