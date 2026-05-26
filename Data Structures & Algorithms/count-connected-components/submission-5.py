class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visit = set()
        def dfs(node):
            if node not in adj:
                return
            if node in visit:
                return
            visit.add(node)
            for nei in adj[node]:
                dfs(nei)
            return
        res = 0
        indegree = {}
        for node in adj:
            indegree[node] = len(adj)
        walk = []
        for node in range(n):
            walk.append(node)
        for i in range(n):
            if i not in visit:
                dfs(i)
                res+=1
        return res