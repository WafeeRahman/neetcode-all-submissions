#Given a 2D grid of integers, where every int is >= 0, find the longest strictly increasing path 
#Where you can move horizontally or vertically
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        #Matrix DFS without Memoizing Subproblems (Saving Solutions to their respective cells per lookup)
        ROWS, COLS = len(matrix), len(matrix[0])
        def dfs(r,c, prev):
            if min(r,c) < 0 or r >= ROWS or c >= COLS:
                return 0
            if matrix[r][c] < prev:
                return 0
            
            res = 0
            if matrix[r][c] > prev:
                prev = matrix[r][c]
                res = 1 + max(dfs(r+1, c, prev), dfs(r-1, c, prev), dfs(r,c+1, prev), dfs(r, c-1, prev))
            return res
        
       
        #We can store solutions in a memocache thats the size of grid, or use a hashmap and store the coordinates
        cache = {}
        def memo(r,c, prev):
            if min(r,c) < 0 or r >= ROWS or c >= COLS:
                return 0
            if matrix[r][c] <= prev:
                return 0
            
            res = 0
            if matrix[r][c] > prev:
                if (r,c) in cache:
                    return cache[(r,c)]
                prev = matrix[r][c]
                res = 1 + max(memo(r+1, c, prev), memo(r-1, c, prev), memo(r,c+1, prev), memo(r, c-1, prev))
            cache[(r,c)] = res
            return res
        
        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                res = max(res, memo(row, col, -1))
        return res

        

 
        