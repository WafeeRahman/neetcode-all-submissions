class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memoC = {}
        ROWS, COLS = len(matrix), len(matrix[0])
        def memo(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 0
            elif (r,c) in memoC:
                return memoC[(r,c)]
            
            
            maxLen = 1
            for dr, dc in [[0,1], [1,0], [0,-1], [-1,0]]:
                if r+dr < 0 or c+dc < 0 or r+dr >= ROWS or c+dc >= COLS or matrix[r+dr][c+dc] <= matrix[r][c]:
                    continue
                curPathLen = 1+memo(r+dr, c+dc)
                maxLen = max(curPathLen, maxLen)
            memoC[(r,c)] = maxLen

            return memoC[(r,c)]
        
        maxPath = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                maxPath = max(maxPath, memo(r,c))
        return maxPath