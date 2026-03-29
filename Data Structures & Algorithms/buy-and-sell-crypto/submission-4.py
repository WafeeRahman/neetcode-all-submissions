class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nums = prices
        res = 0
        l = 0
        for r in range(len(nums)):

            profit = nums[r] - nums[l]
            res = max(res, profit)

            while l<r and profit < 0:
                profit = nums[r] - nums[l]
                res = max(res, profit)
                l+=1
        return res 
            

        