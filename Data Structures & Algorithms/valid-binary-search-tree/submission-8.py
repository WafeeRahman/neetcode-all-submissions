# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lower, upper):
            if not root:
                return True
            
            if not (root.val < upper and root.val > lower):
                return False
            
            validLeft = dfs(root.left, lower, root.val)
            
            validRight = dfs(root.right, root.val, upper)
            
            return (True and validLeft and validRight )
        return dfs(root, float("-infinity"), float("infinity"))

           
       
       
        


         

        
