class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = {}
        for a, b in equations:
            if not b in adj:
                adj[b] = []
            if not a in adj:
                adj[a] = []
        for i, (a, b) in enumerate(equations):
            adj[a].append((b, values[i]))
            adj[b].append((a, 1/values[i]))
        
    
        def dfs(number, weight, target, visit):
            if number not in adj:
                return -1.0
            if number in visit:
                return -1.0
            if number == target:
                return weight
            
            visit.add(number)
            for nei, weight2 in adj[number]:
                if nei in visit:
                    continue
                val = dfs(nei, weight2, target, visit) 
                if val != -1.0:
                    return weight*val
            return -1.0
        res = []
        for query in queries:
            val1 = dfs(query[0], 1.0, query[1], set())
            res.append(val1)
        return  res


            