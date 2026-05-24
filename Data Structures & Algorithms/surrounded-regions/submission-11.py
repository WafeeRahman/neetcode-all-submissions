class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        visit = set()
        def dfs(r,c):
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or board[r][c] == "X" or (r,c) in visit:
                return
            
            board[r][c] = "T"
            visit.add((r,c))
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r-1,c)
            dfs(r,c+1)

        
        for r in range(ROWS):
            dfs(r, COLS-1)
            dfs(r, 0)
        
        for c in range(COLS):
            dfs(0,c)
            dfs(ROWS-1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
            