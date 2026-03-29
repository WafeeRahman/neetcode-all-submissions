class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      res = 0 
      
      def dfs(r, c, visit):
        nonlocal grid
        ROWS, COLS = len(grid), len(grid[0])

        if (min(r,c) < 0 or r == ROWS or c == COLS 
            or grid[r][c] == "0" or (r,c) in visit):
            return 
        

        
        visit.add((r,c))
        grid[r][c] = "0"
   
        #Look for All Reachable Islands
        dfs(r+1, c, visit)
        dfs(r-1, c, visit)
        dfs(r, c+1, visit)
        dfs(r, c-1, visit)
        
        visit.remove((r,c))

        return
      
      path = set()
      for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "1":
                print(grid[row])
                dfs(row, col, path)
                res+=1
               
                
      return res

        

        
