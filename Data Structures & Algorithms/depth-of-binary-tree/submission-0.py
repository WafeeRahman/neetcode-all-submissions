# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #DFS: preorder
        #When theres no children, add zero to the root
        if not root:
            return 0
        
        val1 = self.maxDepth(root.left)
        val2 = self.maxDepth(root.right)

        #If there is a child (root) add 1 to the value
        return 1 + max(val1, val2)
        