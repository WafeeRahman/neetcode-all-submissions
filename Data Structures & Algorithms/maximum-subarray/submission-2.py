#To get the maximum subarray, we can use a greedy method to 
#Calculate the max subarray, and change the subarray we look at based on if our max sum ever becomes negative
#(Kadane's algorithm)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        curSum = 0


        for num in nums:
            if curSum < 0:
                curSum = num
                res = max(res, curSum)
                continue
            
            curSum += num
            res = max(res, curSum)
        
        return res
