# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        def pathSum(root):
            nonlocal res
            if not root:
                return 0
            
            leftMax = max(pathSum(root.left), 0)
            rightMax = max(pathSum(root.right), 0)


            res = max(res, root.val+leftMax+rightMax)

            return root.val + max(leftMax, rightMax)
        pathSum(root)
        return res