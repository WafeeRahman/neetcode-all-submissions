class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        #Topsort to sort by which values are above, and which values are left
        def topSort(edges):
            indegree = [0] * (k+1) #K edges (1-k)
            adj = {}

            #nodes range from 1-k incl
            for node in range(1, k+1):
                adj[node] = []
            
            #Build directed adjlist while incrementing indegree
            for u, v in edges:
                adj[u].append(v)
                indegree[v] += 1
            
            #kahns algorithm
            #Start with the smallest indegrees
            q = deque()
            for i in range(1, k+1):
                if indegree[i] == 0:
                    q.append(i)
            
            res = []
            while q:
                top = q.popleft()
                res.append(top)
                #visit, move onto neighbors and decrement indegrees to traverse
                for nei in adj[top]:
                    indegree[nei] -= 1
                    #traverse the next value whos indegree would be zero if we visit it
                    if indegree[nei] == 0:
                        q.append(nei)
            return res
        
        #take intersection of sorted values
        rowSort = topSort(rowConditions)
        colSort = topSort(colConditions)
        
        #If we cannot sort k values by indegree we cannot get a valid ordering (cycle)
        if len(rowSort) != k or len(colSort) != k:
            return []
        
        #Get the column position for every value
        position = {}
        i=0
        for value in colSort:
            position[value] = i
            i+=1
        res = [[0] * k for _ in range(k)]
        i = 0
        #create rows and column intersection
        #k column mappings and k values in rowSort, will give us a kxk matrix
        for value in rowSort:
            col = position[value]
            res[i][col] = value
            i += 1
        return res