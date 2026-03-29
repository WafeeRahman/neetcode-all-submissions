class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}

        for i in range(n):
            adj[i] = []
        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        def dfs(node, visit):
            if node in visit:
                return False
            
            visit.add(node)
            for nei in adj[node]:
                if nei == node:
                    continue
                dfs(nei, visit)
            return True
        
        count = 0
        for i in range(n):
            if dfs(i, visit):
                count += 1
        return count


            

