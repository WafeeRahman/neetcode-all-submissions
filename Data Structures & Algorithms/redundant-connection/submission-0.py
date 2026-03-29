class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adjList = {}
        for i in range(n+1):
            adjList[i] = []
        
        
        
        
        def dfs(node, visit, parent):
            if node in visit:
                return False
            visit.add(node)
            for nei in adjList[node]:
                if nei == parent:
                    continue
                if not dfs(nei, visit, node):
                    return False
            visit.remove(node)
            return True
        
        visit = set()
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            if not dfs(u, visit, None):
                return [u,v]
        
        return edges[-1]

        

            


