"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloneMap = {}
        def dfs(node):
            if not node:
                return
            if node in cloneMap:
                return
            
            cloneMap[node] = Node(node.val)
            cloneMap[node].neighbors=[]
            for nei in node.neighbors:
                dfs(nei)
                cloneMap[node].neighbors.append(cloneMap[nei])
            
            return cloneMap[node]
        return dfs(node)
