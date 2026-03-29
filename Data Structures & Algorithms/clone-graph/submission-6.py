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
        
        #Build the adjacency list of the original graph
        #With each node value mapping to the neighbor node values
        def buildList(node, visit):
            nonlocal adjList
            #If we've already visited the node, return the node value
            if node in visit:
                return node.val
            
            #OTWS visit node, set it in the adjacency list
            visit.add(node)
            if not node in adjList:
                adjList[node.val] = []
            
            #Add appropriate neighbours to adj list
            
            for neighbor in node.neighbors:
                adjList[node.val].append(buildList(neighbor, visit))
            
            #Backtrack and remove node

            
            #RETN node value to previous call if it wasnt visited
            return node.val
        
        buildList(node, set())
        
        lstCopy = {}
        
        #Afterwards, populate another hashmap with new nodes storing the 
        #original values
        for key in adjList.keys():
            lstCopy[key] = Node(key)
        
        #For each neighbor in the original adj list 
        #Add the neighbour node using the copied nodes 
        #The keys in adj list and lstcopy are the same
        for key in adjList.keys():
            #For each neighbour for each node of the original
            for neighbor in adjList[key]:
                #Append the copy of the neighbour from the original hashmap
                #To the neighbors of the copied node
                lstCopy[key].neighbors.append(lstCopy[neighbor])
        
        return lstCopy[1]
        
            