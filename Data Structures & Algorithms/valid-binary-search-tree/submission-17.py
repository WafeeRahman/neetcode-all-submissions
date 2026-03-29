# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(root, low, high):
            if not root:
                return True
            
            if not low < root.val < high:
                return False
            
            return True and isValid(root.left, low, root.val) and isValid(root.right, root.val, high)
        
        return isValid(root, float("-inf"), float("inf"))
