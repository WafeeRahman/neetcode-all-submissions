class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def topSort(edges):
            indegree = [0] * (k+1) #K edges (1-k)
            adj = {}

            for node in range(1, k+1):
                adj[node] = []

            for u, v in edges:
                adj[u].append(v)
                indegree[v] += 1
            
            q = deque()
            for i in range(1, k+1):
                if indegree[i] == 0:
                    q.append(i)

            res = []
            while q:
                top = q.popleft()
                res.append(top)

                for nei in adj[top]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
            return res

        rowSort = topSort(rowConditions)
        colSort = topSort(colConditions)

        if len(rowSort) != k or len(colSort) != k:
            return []
        
        position = {}
        i=0
        for value in colSort:
            position[value] = i
            i+=1
        res = [[0] * k for _ in range(k)]
        i = 0
        for value in rowSort:
            col = position[value]
            res[i][col] = value
            i += 1
        return res