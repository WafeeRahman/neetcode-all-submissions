class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        level = 0
        visit = set()
        while q:
            for i in range(len(q)):
                node = q.popleft()
                grid[node[0]][node[1]] = level
  
                for dr, dc in dirs:
                    nr, nc = node[0]+dr, node[1]+dc

                    if nr >= len(grid) or nc >= len(grid[0]) or min(nr,nc) < 0 or grid[nr][nc] == -1 or (nr,nc) in visit:
                        continue
                    if grid[nr][nc] == 2147483647:
                        q.append((nr,nc))
                        visit.add((nr,nc))
            level+=1
            
                


            