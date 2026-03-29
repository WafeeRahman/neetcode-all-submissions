# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #Use a global variable to keep track of the current root
        #Preorder Index
        #To take advantage of O(1) lookup time, populate a hashmap w/ values and respective
        #Index in inorder

        #Notice that for each node in preorder, everything in the left subtree is to the left
        #in the inorder list
        preIndex = 0
        inorderMap = {value : index for index, value in enumerate(inorder)}
        
        #Use Two Pointers to traverse the list, and ensure that we dont go out of bounds
        #Relative to what's left of the root node, and what to the right
        def dfs(left, right):
            nonlocal preIndex
            #If our left is >= right, return to the last call
            if left > right or preIndex >= len(preorder):
                return
            
            node_val = preorder[preIndex]
            node = TreeNode(node_val)
            preIndex+=1
            
            #This looks up the index at which the node is located
            #This tells us where the current node at preIndex is in the inorder traversal
            #Using this, we can set its left and right subtrees using the left and right params
            #in the DFS Function
            
            mid = inorderMap[node_val]
            
            node.left = dfs(left, mid-1)
            node.right = dfs(mid+1, right)
            
            return node

        root = dfs(0, len(inorder)-1)
        return root
    
    
            
            
            





        