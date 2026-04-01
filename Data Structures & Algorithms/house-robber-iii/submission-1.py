# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        #Reattempt
        memoC = {}
        def dfs(root, skip):
            if not root:
                return 0
            
            if (root, skip) in memoC:
                return memoC[(root, skip)]
            if skip:
                memoC[(root, skip)] = dfs(root.left, False) + dfs(root.right, False)
            else:
                memoC[(root,skip)] = max((root.val + dfs(root.left, True) + dfs(root.right, True)), (dfs(root.left, False) + dfs(root.right, False)) )
            return memoC[(root, skip)]
        return max(dfs(root, True), dfs(root,False))