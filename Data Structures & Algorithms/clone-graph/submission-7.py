"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        oldToCopy = {node: Node(node.val)}
        q = deque([node])
        visit = set()
       
        while q:
            oldnode = q.popleft()

            for neighbor in oldnode.neighbors:
                if neighbor not in oldToCopy:
                    oldToCopy[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                oldToCopy[oldnode].neighbors.append(oldToCopy[neighbor])
        return oldToCopy[node]
       
        
    
            

            