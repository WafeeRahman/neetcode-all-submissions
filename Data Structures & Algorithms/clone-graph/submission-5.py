"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        grphCopy = {}
        def dfs(node, visit):
            nonlocal grphCopy
            #If we already visited the node, we don't need to 
            #init a copy, therefore return the appropriate copy
            if node in visit:
                return grphCopy[node]
            
            #Store a copy of each node in a hashmap
            visit.add(node)
            grphCopy[node] = Node(node.val)
            
            #For each visited node, append the neighbor's copies 
            #To the copied node's neighbor list
            for neighbor in node.neighbors:
                grphCopy[node].neighbors.append(dfs(neighbor, visit))
            

            return grphCopy[node]
        dfs(node, set())
        
        return grphCopy[node]



