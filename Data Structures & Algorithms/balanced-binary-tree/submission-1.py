# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0] #Balanced, Height Value
            
            balanced = not abs(dfs(root.left)[1] - dfs(root.right)[1]) > 1

            return [(balanced and dfs(root.left)[0] and dfs(root.right)[0]), 1+max(dfs(root.right)[1], dfs(root.left)[1])]

        return dfs(root)[0]      
