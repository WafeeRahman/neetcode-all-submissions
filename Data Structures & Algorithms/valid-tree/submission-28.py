class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {}
        for i in range(n):
            adj[i] = []
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visit = set()
        cycle = set()
        def dfs(node, prev):
            if node in cycle:
                return False
            if node in visit:
                return True
            
            
            cycle.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            cycle.remove(node)
            visit.add(node)
            return True
        return dfs(0, -1) and len(visit) == n