# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if root.val == subRoot.val:
            print(root.val, subRoot.val)
            val = self.subDFS(root, subRoot)
            if val:
                return val
        

        return (False or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    
    
    
    
    
    def subDFS(self, root, subroot):
        if (not root) and (not subroot):
            return True
        if (not root) or (not subroot):
            return False
        if root.val != subroot.val:
            return False
        
        return (True and self.subDFS(root.left, subroot.left) and self.subDFS(root.right, subroot.right))
            
            
