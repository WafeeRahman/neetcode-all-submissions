class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowCheck = defaultdict(set)
        colCheck = defaultdict(set)
        squareCheck = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                cell = board[i][j]
                if cell == ".":
                    continue
                if cell in rowCheck[i] or cell in colCheck[j] or cell in squareCheck[(i//3, j//3)]:
                    return False
                else:
                    rowCheck[i].add(cell)
                    colCheck[j].add(cell)
                    squareCheck[(i//3, j//3)].add(cell)
                    continue
        return True
                