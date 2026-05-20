class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = {}
        for i in range(1, n+1):
            adj[i] = []
        for a, b in trust:
            adj[a].append(b)
        
        townJudge = None
        for key in adj:
            if adj[key] == []:
                if townJudge:
                    return -1
                townJudge = key
        
        for key in adj:
            if key != townJudge:
                if townJudge not in adj[key]:
                    print(adj[key], key)
                    return -1
        return townJudge 