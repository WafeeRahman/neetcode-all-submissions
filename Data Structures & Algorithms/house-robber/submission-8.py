class Solution:
    def rob(self, nums: List[int]) -> int:
        res = 0
        def dfs(i):
            if i >= len(nums):
                return 0
            
            return max((dfs(i+2) + nums[i]), (dfs(i+1)))

        cache = {}
        def memo(i):
            nonlocal cache
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            
            cache[i] = max((memo(i+2) + nums[i]), (memo(i+1)))
            return cache[i]
        
        return memo(0)

       