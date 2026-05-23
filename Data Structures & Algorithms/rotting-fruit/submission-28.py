class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        fruit = 0
        rotten = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 or grid[r][c] == 2:
                    fruit+=1
                    if grid[r][c] == 2:
                        rotten+=1
                        q.append((r,c))
        if fruit and not rotten:
            return -1
        if not rotten:
            return 0

        dirs = [[0,1], [1,0], [-1,0], [0,-1]]
        visit = set()
        level = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                if grid[r][c] == 1:
                    rotten += 1
                if rotten == fruit:
                    return level


                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if nr >= ROWS or nc >= COLS or nr < 0 or nc < 0 or grid[nr][nc] == 0 or (nr,nc) in visit:
                        continue
                    q.append((nr,nc))
                    visit.add((nr,nc))
            level += 1
        return -1
