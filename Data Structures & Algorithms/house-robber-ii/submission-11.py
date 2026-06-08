class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def dp(arr):
            
            memo = {}
            n = len(arr)
            def dfs(i, canRob):
                if i >= n:
                    return 0
                if (i, canRob) in memo:
                    return memo[(i, canRob)]
                noRob = 0
                rob = 0
                if canRob:
                    rob = arr[i] + dfs(i+1, False)
        
                noRob = dfs(i+1, True)
                
                memo[(i, canRob)] = max(rob, noRob)
                
                return memo[(i, canRob)]
           
            dfs(0, True)
            return memo[(0, True)]
        return max(dp(nums[0:len(nums)-1]), dp(nums[1:]))
    