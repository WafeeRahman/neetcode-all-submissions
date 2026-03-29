class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fruit = 0
        maxLen = float("inf")
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] != 0:
                    fruit += 1
        
        if fruit == 0:
            return 0
        
        def bfs(grid, r, c, visit):
            nonlocal ROWS, COLS, fruit
            q = deque([])
            curRotFruit = 0
            
            for row in range(ROWS):
                for col in range(COLS):
                    if grid[row][col] == 2:
                           q.append((row,col))
                           visit.add((row,col))

            
            minutes = 0             
            print(q)
            while q:
                for i in range(len(q)):
                    r,c = q.popleft()
                    
                    if grid[r][c] != 0:
                        curRotFruit += 1
                        print(curRotFruit, fruit)
                        grid[r][c] = 2

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
        


