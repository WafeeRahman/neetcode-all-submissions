class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {}
        
        
        visit = set()
        def dfs(node, par):
            if node in visit:
                return False
            
            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                elif not dfs(nei, node):
                    return False
            visit.remove(node)
            return True
            
        for a, b in edges:
            if not a in adj:
                adj[a] = []
            if not b in adj:
                adj[b] = []
            adj[a].append(b)
            adj[b].append(a)

            if not dfs(a,b):
                return [a,b]
   