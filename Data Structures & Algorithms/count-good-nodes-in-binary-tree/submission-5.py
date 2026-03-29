# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0
        def dfs(root, onGoingMax):
            nonlocal res

            if not root:
                return

            if root.val >= onGoingMax:
                onGoingMax = root.val
                res+=1
            dfs(root.left, onGoingMax)
            dfs(root.right, onGoingMax)
        dfs(root, float('-inf'))
        return res