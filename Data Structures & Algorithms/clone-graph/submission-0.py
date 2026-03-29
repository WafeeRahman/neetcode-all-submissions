"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #Build Adj List
        adjList = {}
        if not node:
            return None
        def buildList(node, visit):
            nonlocal adjList
            
            if node in visit:
                return node.val
            
            visit.add(node)
            if not node in adjList:
                adjList[node.val] = []
            
            for neighbor in node.neighbors:
                adjList[node.val].append(buildList(neighbor, visit))
            
            visit.remove(node)
            
            return node.val
        buildList(node, set())
        
        lstCopy = {}
        #Copy By Value
        for key in adjList.keys():
            lstCopy[key] = Node(key)
        
        for key in adjList.keys():
            for neighbor in adjList[key]:
                lstCopy[key].neighbors.append(lstCopy[neighbor])
        
        return lstCopy[1]
        
            
            