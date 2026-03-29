class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      res = 0 
      
      #Use Matrix DFS to eliminate all adjacent entries of one
      #Counting each group elimination
      def dfs(r, c, visit):
        nonlocal grid
        ROWS, COLS = len(grid), len(grid[0])

        #If we find a zero, continue as we're searching for adjacent ones
        if (min(r,c) < 0 or r == ROWS or c == COLS 
            or grid[r][c] == "0" or (r,c) in visit):
            return 
        
        #Add to Path
        visit.add((r,c))
        grid[r][c] = "0"
   
        #Look for All Reachable Islands
        dfs(r+1, c, visit)
        dfs(r-1, c, visit)
        dfs(r, c+1, visit)
        dfs(r, c-1, visit)
        
   
        return
      

      for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "1":
                print(grid[row])
                dfs(row, col, set())
                res+=1
               
                
      return res

        

        
