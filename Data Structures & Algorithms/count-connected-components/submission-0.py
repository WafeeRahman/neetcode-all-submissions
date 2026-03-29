class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {}
        for i in range(n): 
            adjList[i] = []

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        

        def dfs(node, visit):
            if node in visit:
                return
            visit.add(node)
            for nei in adjList[node]:
                if nei == node:
                    continue
                dfs(nei, visit)
        
        compCount = 0
        visit = set()
        for i in range(n):
            if i not in visit:
                dfs(i, visit)
                compCount +=1
        return compCount


        