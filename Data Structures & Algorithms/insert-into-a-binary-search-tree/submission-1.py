# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        prev = None
        def dfs(root):
            nonlocal prev
            if not root:
                return
            prev=root
            if val > root.val:
                dfs(root.right)
            elif val < root.val:
                dfs(root.left)
            return prev
        dfs(root)
        if not root:
            return TreeNode(val)
        if val > prev.val:
            prev.right = TreeNode(val)
        elif val < prev.val:
            prev.left = TreeNode(val)
        return root