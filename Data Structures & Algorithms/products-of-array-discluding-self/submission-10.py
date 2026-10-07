class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1

        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] = prefix
            prefix*=nums[i]
 
        postfix = 1

        for j in range(len(nums)-1,-1,-1):
            res[j] *= postfix
            postfix *= nums[j]
        
        return res