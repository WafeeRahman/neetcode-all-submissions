"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        ROWS = len(grid) 
        COLS = len(grid[0])
        def dfs(r,c,n):
        
            if r >= ROWS or c >= COLS:
                return None
            if n==1:
                return Node(grid[r][c], True)
            n=n//2
            topLeft = dfs(r,c,n)
            topRight= dfs(r,c+n, n)
            bottomLeft = dfs(r+n,c,n)
            bottomRight = dfs(r+n,c+n,n)

            if topLeft.isLeaf and bottomLeft.isLeaf and topRight.isLeaf and bottomRight.isLeaf and \
            topLeft.val == bottomLeft.val == topRight.val == bottomRight.val:
                return Node(grid[r][c], True)
            else:
                return Node(grid[r][c], False, topLeft, topRight, bottomLeft, bottomRight)
        return dfs(0,0, ROWS)

