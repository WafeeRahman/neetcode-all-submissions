class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adjList = {}

        #Build Adjacency List w/ Edges
        
        for edge in edges:
            if edge[0] not in adjList:
                adjList[edge[0]] = []
            if edge[1] not in adjList:
                adjList[edge[1]] = []
            
            #If the graph is undirected, that means 
            #The relation is reflexive and goes both directions
            
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        #Use DFS to check if the graph has a cycle that where
        #the vertex shares a cycle with a node thats not its parent
        def dfs(node, visit, parentNode):
            nonlocal adjList
            
            #If we've already visited a node, dont revisit and return false
            if node in visit:
                return False
            
            visit.add(node)

            for neighbor in adjList[node]:
                #Run DFS on each neighbouring node
                #If we already visited a neighbor, there may be a cycle
                #If there was a case where we're revisiting a node
                
                if not dfs(neighbor, visit, node):
                    
                    #We can only have a cycle with the parent node in a tree
                    #As the graph is undirected
                    
                    if neighbor != parentNode:
                        
                        #If the neighbor is not the parent node, then that indicates
                        #Theres a cycle in the undirected graph
                        
                        return False
            
            #Dont Backtrack, as we're checking the set built in dfs 
            #And if we have visited every node per dfs
            return True
        
        #For every node in the graph, run DFS, and check if the theres a non parent cycle
        #If the DFS succeeds, check if every vertex is visited (connected graph)
        if not edges:
            return True
        visit = set()   
        if not dfs(0, visit, None):  #There's no parent node for the first node
            return False
        if len(visit) != n:
            return False
        return True

        