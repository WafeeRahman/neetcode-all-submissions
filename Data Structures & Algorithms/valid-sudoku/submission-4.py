class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colSet = defaultdict(set) #Set for each col (no dupes)
        rowSet = defaultdict(set) #Set for each row (no dupes)
        boardSet = defaultdict(set) #Set for each 3x3 board
        
        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue 
                if board[r][c] in rowSet[r] or board[r][c] in colSet[c] or board[r][c] in boardSet[(r//3,c//3)]:
                    return False
                
                rowSet[r].add(board[r][c])
                colSet[c].add(board[r][c])
                boardSet[(r//3,c//3)].add(board[r][c])
        return True