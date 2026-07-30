class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = max(nums)
        for i in range(len(nums)):
            if curSum < 0:
                curSum = 0
            curSum += nums[i]
            maxSum = max(curSum, maxSum)
            
            
        
        #circular case, total sum - minimum contigous subarray could be the max
        curMin = 0
        minMin = min(nums)
        for i in range(len(nums)):
            curMin=min(curMin + nums[i], nums[i])
            minMin = min(curMin, minMin)
        #cant subtract a negative sum from a negative sum
        if maxSum < 0:
            return maxSum
        return max(maxSum, sum(nums)-minMin)