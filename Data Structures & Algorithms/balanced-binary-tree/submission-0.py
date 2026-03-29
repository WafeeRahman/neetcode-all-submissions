# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        val1 = self.getHeight(root.left)
        val2 = self.getHeight(root.right)

        if abs(val1 - val2) > 1:
            return False
        
        return (True and self.isBalanced(root.left) and self.isBalanced(root.right))
    

    def getHeight(self, root):
        if not root:
            return 0
        
        return 1+(max(self.getHeight(root.left), self.getHeight(root.right)))