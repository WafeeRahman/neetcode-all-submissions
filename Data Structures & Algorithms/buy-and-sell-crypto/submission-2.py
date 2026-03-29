class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nums = prices
        l = 0 
        maxP=0
        for r in range(l+1, len(nums)):
            profit=nums[r]-nums[l]
            maxP = max(maxP, profit)
            #Sliding Condition
            while profit < 0:
                l+= 1
                profit=nums[r]-nums[l]
        return maxP
        