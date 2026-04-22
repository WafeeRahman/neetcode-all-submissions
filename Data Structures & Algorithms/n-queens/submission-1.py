class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ROWS = n
        COLS = n

        colset = set()        
        posDiag = set()     
        negDiag = set()
        board = [["."] * n for _ in range(n)]
        res = []
        def backtrack(r, q):

            if r == ROWS:
                if q == n:
                    res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
      
                if (r+c) in posDiag or (r-c) in negDiag or c in colset:
                    continue
                else:
                    colset.add(c)
                    posDiag.add((r+c))
                    negDiag.add((r-c))
                    board[r][c] = "Q"
                    backtrack(r+1, q+1)
                    board[r][c] = "."
                    colset.remove(c)
                    posDiag.remove((r+c))
                    negDiag.remove((r-c))
            return
        backtrack(0,0)
        return res