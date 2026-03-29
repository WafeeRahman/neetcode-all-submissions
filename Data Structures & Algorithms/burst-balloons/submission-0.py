class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #Bordering 1's for Base Case, where the final value is popped and there are no adj balloons

        nums = [1] + nums + [1]

        dp = {}


        def dfs(l,r):
            #If we popped all of the balloons
            if l > r:
                return 0 
            #Cache Lookup
            if (l,r) in dp:
                return dp[(l,r)]
            
            dp[(l, r)] = 0
            for i in range(l, r+1):
                #Compute the Amount of Coins if we popped the current baloon last
                coins = nums[i] * nums[r+1] * nums[l-1]
                coins += dfs(l, i-1)
                coins += dfs(i+1, r)
                dp[(l,r)] = max(dp[(l,r)], coins)
            
            return dp[(l,r)]
            



        return dfs(1, (len(nums)-2))
            