# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p and q:
                return False
            if p and not q:
                return False
            
            return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
      
        exists = False
        def dfs(root):
            nonlocal exists
            if not root:
                return
            
            if root.val == subRoot.val:
                exists = exists or isSameTree(root, subRoot)
            
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return exists
            
            
        