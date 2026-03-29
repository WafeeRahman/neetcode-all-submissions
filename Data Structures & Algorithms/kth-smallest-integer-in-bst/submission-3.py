# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        kthSmallest = None
        def dfs(root):
            nonlocal count
            nonlocal kthSmallest
            if not root:
                return
            
            dfs(root.left)
            print(root.val)
            count+=1
            print(count)

            if count == k:
                kthSmallest = root.val

            dfs(root.right)
        dfs(root)

        return kthSmallest


            
