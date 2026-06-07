class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}


        def dfs(i, canRob):
            if i >= n:
                return 0
            elif (i,canRob) in memo:
                return memo[(i,canRob)]
            
            rob = 0
            noRob = 0
            if canRob: #rob this house
                rob = nums[i] + dfs(i+1, False)
           
            noRob = dfs(i+1, True)
            memo[(i, canRob)] = max(rob, noRob)
           
                
            return memo[(i, canRob)]
        
        dfs(0, True)
        dfs(0, False)
        return max(memo[(0, False)], memo[(0, True)])
            
        