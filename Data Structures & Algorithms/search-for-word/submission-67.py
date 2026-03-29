class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        buildWord = []
        path = set()
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r, c, i):
            nonlocal buildWord, word
            nonlocal path, ROWS, COLS

            if i == len(word):
                return True
            
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS 
                
                or (r,c) in path or i >= len(word) or
                
                board[r][c] != word[i] 
                
            ):
                
                return False
            
            print(board[r][c], word[i], i)
           
            buildWord.append(str(board[r][c]))
            i+=1
        
            path.add((r,c))
            
            print(path, buildWord, i)
            
            if dfs(r+1,c,i) or dfs(r-1,c,i) or dfs(r,c+1,i) or dfs(r,c-1,i):
                return True

            path.remove((r,c))
            buildWord.pop()
            i-=1

            return False

            
            
    
        
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True
        return False

            








        