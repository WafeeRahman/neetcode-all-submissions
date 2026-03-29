class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #MULTI SOURCE BFS SOLUTION
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque([])
        INF = 2147483647
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        
        length = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if grid[r][c] == INF:
                    grid[r][c] = length

                neibs = [[1,0], [-1,0], [0,1], [0,-1]]

                for dr, dc in  neibs:
                    nr, nc = r+dr, c+dc

                    if (min(nr, nc) < 0 or nr == ROWS or nc == COLS 
                        or (nr,nc) in visit or grid[nr][nc] == -1):
                        continue

                    q.append((nr,nc))
                    visit.add((nr,nc))

            length+=1               






        