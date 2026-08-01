class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        adj = {}
        for i in range(len(nums)):
            adj[i] = []
        import math

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if math.gcd(nums[i], nums[j]) > 1:
                    adj[i].append(j)
                    adj[j].append(i)

        
        visit = set()

        def dfs(node):
       
            visit.add(node)
            for nei in adj[node]:
                if nei in visit:
                    continue
                dfs(nei)

        dfs(0)
        return len(visit) == len(nums)
