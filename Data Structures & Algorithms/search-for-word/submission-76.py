class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        curWord = []
        def dfs(r, c, i):
            if i >= len(word):
                return True
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or (r,c) in visit:
                return False
            if board[r][c] != word[i]:
                return False
            
            visit.add((r,c))
            if board[r][c] == word[i]:
                if dfs(r+1, c, i+1) or dfs(r, c+1, i+1) or dfs(r-1, c, i+1) or dfs(r, c-1, i+1):
                    return True
            visit.remove((r,c))
            return False

        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    visit = set()
                    if dfs(r,c,0):
                        return True
        return False
            
            
            
