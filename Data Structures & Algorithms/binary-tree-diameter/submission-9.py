# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0

        def dfs(root):
            nonlocal maxDiameter
            if not root:
                return 0
            maxDiameter = max(maxDiameter, (dfs(root.left) + dfs(root.right)))
            return 1 + max(dfs(root.left), dfs(root.right))
        dfs(root)
        return maxDiameter
        