class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        ROWS, COLS = len(heights), len(heights[0])
        def dfs(heights, r, c, visit, target, prevCell):
            nonlocal ROWS, COLS
            
            #If we already visited or we're out of bounds
            if (min(r, c) < 0 or r == ROWS or c == COLS or (r,c) in visit or 
               prevCell < heights[r][c]):
                return False

            visit.add((r,c))

            #If we reach the target border
            #Row = 0 or Col = 0 for atlantic
            #Row = N or C = n for Pacific
            if r == target[0] or c == target[1]:
                return True
            
            if (dfs(heights, r+1, c, visit, target, heights[r][c]) or
                dfs(heights, r-1, c, visit, target, heights[r][c]) or
                dfs(heights, r, c+1, visit, target, heights[r][c]) or
                dfs(heights, r, c-1, visit, target, heights[r][c])):
                return True
    
            return False
        
        #Try to Verify DFS for each cell and border
        for r in range(len(heights)):
            for c in range(len(heights[r])):
                if (dfs(heights, r, c, set(), [0,0], heights[r][c]) 
                and dfs(heights,r,c,set(),[ROWS-1, COLS-1], heights[r][c])):
                    res.append([r,c])
        return res

            


                