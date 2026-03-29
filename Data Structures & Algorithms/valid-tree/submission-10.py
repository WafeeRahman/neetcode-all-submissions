class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adjList = {}

        for edge in edges:
            if edge[0] not in adjList:
                adjList[edge[0]] = []
            if edge[1] not in adjList:
                adjList[edge[1]] = []
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        nodeSet = set()
        for key in adjList.keys():
            nodeSet.add(key)

    
        def dfs(node, visit, parentNode):
            nonlocal adjList
            
            if node in visit:
                return False
            
            visit.add(node)

            for neighbor in adjList[node]:
                if not dfs(neighbor, visit, node):
                    if neighbor != parentNode:
                        return False
            
            return True
        
        for node in nodeSet:
            visit = set()
            if not dfs(node, visit, None):
                return False
            if visit != nodeSet:
                return False
        return True

        