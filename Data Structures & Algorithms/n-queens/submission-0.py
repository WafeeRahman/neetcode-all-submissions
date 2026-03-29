class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for i in range(n)]
        #Utilize a set for columns, positive diag
        #Each queen will have a different row, there will never be queens in the same row
        #As they can be attacked from left or right
        colSet = set() #Maintain columns, as we need to make sure there are no
                       #Vertically adjacent queens
        #Ensure that queens arent adjacent diagonally in both left and right directionsl
        posDiag = set()
        negDiag = set()
     
        def backtrack(r):
            #If we reach the end of the row without
            #Reaching a case where placing a queen wasnt safe
            
            if r == n:
                print(board)
                copy = board.copy()
                subcopy = []
                for i in range(r):
                    subcopy.append("".join(copy[i]))
                res.append(subcopy)
                return

        
            #Iterate through the columns of each row
            for c in range(n):
                if c in colSet or r-c in negDiag or r+c in posDiag:
                    continue
                board[r][c] = 'Q'
                
                
                colSet.add(c)
                negDiag.add(r-c)
                posDiag.add(r+c)
                #Check the next row
                backtrack(r+1)
                #Check other possibilities
                board[r][c] = "."
                colSet.remove(c)
                negDiag.remove(r-c)
                posDiag.remove(r+c)
        
        backtrack(0)
        print(res)
        return res


            


        