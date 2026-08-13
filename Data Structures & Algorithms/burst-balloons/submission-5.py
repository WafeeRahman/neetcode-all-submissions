class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums.insert(0, 1)
        nums.append(1)
        
        
        dp = [[0] * len(nums) for _ in range(len(nums))]
        
        for l in range(n, 0, -1):
            for r in range(l, n+1):
                for i in range(l, r+1):
                    coins = nums[i] * nums[l-1] * nums[r+1] 
                    coins += dp[l][i-1]
                    coins += dp[i+1][r]
                    dp[l][r] = max(dp[l][r], coins)
        return dp[1][n]

        









        """
        memoC = {}

        def memo(left, right):
            if (left, right) in memoC:
                return memoC[(left, right)]
            if left+1 == right:
                return 0
            

            best = 0
            for i in range(left+1, right):
                lft = nums[left]
                rght = nums[right]
                pop = nums[i] * lft * rght
                pop += memo(left, i)
                pop += memo(i, right)

                best = max(best, pop)
            memoC[(left, right)] = best
            return memoC[(left, right)]
        return memo(0, len(nums)-1)
        """