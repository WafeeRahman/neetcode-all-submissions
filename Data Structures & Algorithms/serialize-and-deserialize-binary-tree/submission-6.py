# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        pathSTR = ""
        def dfs(root):
            nonlocal pathSTR 
            if not root:
                pathSTR += "N" + ","
                return
            
            pathSTR+=str(root.val)+","
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return pathSTR


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        data = data.split(",")
        i = 0
        def dfs():
            nonlocal i
            if i >= len(data):
                return
            if data[i] == "N":
                i+=1
                return
            Node = TreeNode(int(data[i]))
            i+=1
            Node.left = dfs()
            Node.right = dfs()

            return Node
        root = dfs()
        return root

