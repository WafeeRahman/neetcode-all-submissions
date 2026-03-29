# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        if not root:
            return -1
        def dfs(root):
            if not root:
                return
            nonlocal count
            result = dfs(root.left)
            count+=1
            
            
            if count == k:
                return root.val
            
            if not result:
                result = dfs(root.right)
            return result

        
        return dfs(root)
        