class Solution:
    def totalNQueens(self, n: int) -> int:
        colSet = set()
        posDiag = set()
        negDiag = set()

        sols = 0
        def backtrack(r,q):
            nonlocal sols
            if r >= n:
                if q == n:
                    sols+=1
                return
            
            

            for c in range(n):
                if c in colSet or r+c in posDiag or r-c in negDiag:
                    continue
                colSet.add(c)
                posDiag.add((r+c))
                negDiag.add((r-c))
                backtrack(r+1, q+1)

                colSet.remove(c)
                posDiag.remove((r+c))
                negDiag.remove((r-c))
        backtrack(0,0)
        return sols