# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            
            leftPathSum = dfs(root.left)
            rightPathSum = dfs(root.right)
            #Take Maxes to Remove Negatives
            leftMax = max(leftPathSum, 0)
            rightMax = max(rightPathSum, 0)

            #Max Path With Splitting - Root Value + the MaxPaths of the left and Right
            currentPathSum = root.val + leftMax + rightMax
            res = max(res, currentPathSum)

            return root.val + max(leftMax, rightMax)
            
        dfs(root)

        return res
           


    
            