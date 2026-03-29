class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #Product Except Self for each val = prod of all nums preceding (left)
        #X Product of all succeeding vals (right)
        #We can do this in two loops

        prefix = 1
        res = nums[:]
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        print(res)
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i] * postfix
            postfix *= nums[i]

        return res