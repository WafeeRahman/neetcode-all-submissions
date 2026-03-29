class Solution:
    def climbStairs(self, n: int) -> int:    
        def memoization(val, cache):
            #Base Case for uncached calls
            if val >= n:
                if val == n:
                    #Return 1 to signify theres a valid path
                    return 1
                return 0
            #Lookup Cached Solutions
            if val in cache:
                return cache[val]
            
            #Cache a solution by calling up the respective paths to the basecase
            cache[val] = memoization(val+1, cache) + memoization(val+2, cache)

            #Return the cached paths for the original value
            return cache[val]
        def dp(n):
            if n <= 2:
                return n
            dp = [0] * (n+1)
            dp[1] = 1
            dp[2] = 2

            for i in range(3, n+1):
                dp[i] = dp[i-1] + dp[i-2]
            return dp[n]
        return dp(n)


            




        