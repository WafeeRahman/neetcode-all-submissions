class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        Rows = len(board)
        Cols = len(board[0])

        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        boardSet = defaultdict(set)
        for r in range(Rows):
            for c in range(Cols):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rowSet[r]:
                    return False
                elif board[r][c] in colSet[c]:
                    return False
                elif board[r][c] in boardSet[(r//3,c//3)]:
                    return False
                
                rowSet[r].add(board[r][c])
                colSet[c].add(board[r][c])
                boardSet[(r//3, c//3)].add(board[r][c])
        return True
