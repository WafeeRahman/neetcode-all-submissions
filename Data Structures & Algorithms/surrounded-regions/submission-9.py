class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c, visit):
            nonlocal ROWS, COLS
            if (min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visit or board[r][c] == "X"):
                return 
            
            board[r][c] = "#"
            visit.add((r,c))
            
            #DFS Adjacent Regions
       
            dfs(r+1,c,visit)
            dfs(r-1,c,visit)
            dfs(r,c+1,visit)
            dfs(r,c-1,visit)
        
        #Clear Bordering Os
        for c in range(COLS):
            if board[0][c] == "O":
                board[0][c] = "T"
            
            if board[ROWS-1][c] == "O":
                board[ROWS-1][c] = "T"
        
        for r in range(ROWS):
            if board[r][0] == "O":
                board[r][0] = "T"
            
            if board[r][COLS-1] == "O":
                board[r][COLS-1] = "T"
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "T":
                    dfs(row, col, set())
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    board[row][col]  = "X"
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "T" or board[row][col] == "#":
                    board[row][col]  = "O"

            

     



