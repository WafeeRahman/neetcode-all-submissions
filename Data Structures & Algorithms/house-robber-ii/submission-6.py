class Solution:
    def rob(self, nums: List[int]) -> int:
        #Use a flag to signify if the first house was robbed or not        
        def dfs(i, flag):
            #If we robbed all of the houses
            #Or we robbed the first house and cant rob the last house
            #Return Zero
            if i >= len(nums) or (i == len(nums)-1 and flag):
                return 0
            #If we're on the path where we robbed the first house, explore 
            #robbing the current house vs the next
            if flag:
                return max((dfs(i+2, True) + nums[i]), dfs(i+1, True))
            #If we're on the path where didnt rob the first house, explore 
            #robbing the current house vs the next
            elif flag == False:
                return max((dfs(i+2, False) + nums[i]), dfs(i+1, False))
            
            #Take the max of the two paths, starting at the first house vs not starting at the first house
            return max(dfs(0, True), dfs(1, False))

        
        #Use a cache for memoization
        cache = {}

        def memo(i, flag):
            nonlocal cache
            #If there's only one house, rob it
            if len(nums) == 1:
                return nums[0]
            #
            if i >= len(nums) or (i == len(nums)-1 and flag):
                return 0
                
            #If the current flag  and i are in the cache, look it up
            if (i, flag) in cache:
                return cache[i, flag]
            else:
                #For each function call, cache the true path values and the false path values
                #To save on repeated work 
                if flag == True:
                    cache[(i, flag)] = max((memo(i+2, True) + nums[i]), memo(i+1, True)) 
                elif flag == False:
                    cache[(i, flag)] = max((memo(i+2, False) + nums[i]), memo(i+1, False))
            return cache[(i, flag)]
        
        def dp(nums):
            #dp[i] = max(dp[i-2] + cost[i], dp[i-1])
            prev1 = 0
            prev2 = 0
            for i in range((len(nums))):
                currentMaxProfit = max(prev1, (prev2 + nums[i]))
                prev2 = prev1
                prev1 = currentMaxProfit
            return prev1
        
        def dpSolution(nums):
            if len(nums) == 1:
                return nums[0]
            return max(dp(nums[:len(nums)-1]), dp(nums[1:]))
        
        return dpSolution(nums)
        



