class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curProfit = 0
        nums = prices
        for i in range(len(nums)):
            if i < len(nums)-1 and nums[i] < nums[i+1]:
                curProfit += nums[i+1] - nums[i]
        return curProfit
