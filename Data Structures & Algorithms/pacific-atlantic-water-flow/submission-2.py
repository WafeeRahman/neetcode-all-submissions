class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        ROWS, COLS = len(heights), len(heights[0])
        def dfs(heights, r, c, visit, prevCell):
            nonlocal ROWS, COLS
            
            #If we already visited or we're out of bounds
            #Start at Borders, ensuring that the encountered
            #Cells are less than the previous, as we started at the border
            #Creating path sets where each encountered cell is less than or equal to the
            #Previous, but actively searching the opposite
            if (min(r, c) < 0 or r == ROWS or c == COLS or (r,c) in visit or 
               prevCell > heights[r][c]):
               return
                

            visit.add((r,c))

            
            #Exhaust Search
            dfs(heights, r+1, c, visit,  heights[r][c]) 
            dfs(heights, r-1, c, visit,  heights[r][c]) 
            dfs(heights, r, c+1, visit,  heights[r][c]) 
            dfs(heights, r, c-1, visit,  heights[r][c])
            
    
           
        
        pac, atl = set(), set()
        
        #Instead of brute force searching, we can build sets of each vertex in the
        #That can reach the atlantic, and each that can reach the pacific
        #The intersection is our result

        #Build DFS sets by traversing starting from Pacific and Atlantic Columns
        #Leftmost and Rightmost columns
        for c in range(COLS):
            dfs(heights, 0, c, pac,  heights[0][c])
            dfs(heights, ROWS-1, c, atl, heights[ROWS-1][c])
        
        #Build DFS sets by traversing starting from Pacific and Atlantic rows
        #Top and Bottom rows
        for r in range(ROWS):
            dfs(heights, r, 0, pac, heights[r][0])
            
            dfs(heights, r, COLS-1, atl,  heights[r][COLS-1])
        
        #If there were no solutions in DFS, that would mean that the set intersection is 
        #EMPTY.

        for r in range(ROWS):
            for c in range(COLS):
                #If a given cell is in both paths, that means that they can reach
                #Both the pacific and atlantic
                if (r,c) in pac and (r, c) in atl:
                    res.append([r,c])

        return res

            


                