class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        #bottom up dynamic programming, we can start at the base case and work our way up to o, o moving left and up
        prevRow = [1] * n #For each column and row there is a unique path, default value of one

        #Start from 0,0, and build subproblem solutions that depend on the solution from the previous row (1 step down)
        #And the adjacent column to the right (right)
        for r in range(m-1):
            curRow = [1]*n
            
            for c in range(n-2,-1,-1):
                prevCellR = prevRow[c] #Paths from bottom
                prevCellC = curRow[c+1] if c < n else 0 #Paths from right
                curRow[c] = prevCellR + prevCellC
            prevRow = curRow
        return prevRow[0]



        