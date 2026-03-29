class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
     
        
        
       
        def bfs(grid, r, c, visit):
            nonlocal ROWS, COLS
            q = deque([])
            curRotFruit = 0
            fruit = 0

            #Count the amount of fruit in grid for exit condition
            #And append any rotten fruit to queue for multi source BFS
            for row in range(ROWS):
                for col in range(COLS):
                    if grid[row][col] != 0:
                            fruit += 1
                    if grid[row][col] == 2:
                           q.append((row,col))
                           visit.add((row,col))

            #Amount of minutes before rotting is the distance in edges between
            #Rotten and unrotten fruit
            minutes = 0             
            while q:
                for i in range(len(q)):
                    r,c = q.popleft()
                    
                    #If we encounter a fruit
                    if grid[r][c] != 0:
                        curRotFruit += 1
                        print(curRotFruit, fruit)
    
                    if curRotFruit == fruit:
                        return [curRotFruit==fruit,minutes]
                    
                    neibs = [[1,0],[-1,0],[0,1],[0,-1]]

                    for dr, dc in neibs:
                        nr, nc = r+dr, c+dc
                        if (min(nr,nc) < 0 or nr == ROWS or nc == COLS or (nr, nc) in visit
                            or grid[nr][nc] == 0):
                            continue
                        q.append((nr,nc))
                        visit.add((nr,nc))

                minutes += 1
            
            print(curRotFruit, fruit)
            return [curRotFruit==fruit,minutes]

        search=bfs(grid, 0, 0, set()) 
        
        return search[1] if search[0] else -1    
        
        return maxLen if maxLen != float("inf") else -1
        


