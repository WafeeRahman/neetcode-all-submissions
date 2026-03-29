#With an array nums, find the subarray with the maximum product, returning the maximum product
#A Subarray is a contigous sequence within the array, where the order of each element is preserved, with no deletions
#We can use an edited version of kadanes algorithm, which originally calculates the maximum sum of a subarray
#And changes the window based on of the current sum is less than zero

#Here, things are a bit different, as two negative values can create a positive value
#To address this, we can take the current maximum product, aswell as the current minimum product
#At each step, the current maximum product can be: the current maximum * the ith number, the minimum * ith number iff the ith number is -ve
#Or the ith number itself.
#Its also important to skip zeroes, as if our curmax ever becomes zero, it will zero every value that is multiplied to it
#instead, reset the windows
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = max(nums)
        curMax = 1
        curMin = 1
        
        for num in nums:
            if num == 0:
                curMax = 1
                curMin = 1
                continue
            curProd = curMax * num
            curMax = max(curProd, curMin *num, num)
            curMin = min(curProd, curMin*num, num)
            res = max(curMax, res)

        return res if res != float('inf') else 0
        
        
