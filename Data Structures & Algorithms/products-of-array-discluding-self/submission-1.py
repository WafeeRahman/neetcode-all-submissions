class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preFixProd = 1
        postFixProd = 1

        res = [1] * len(nums)
        
        for i in range(len(nums)):
            # Get the preFix product for each number, (product of all preceding numbers before each value non inclusive)
            res[i] = preFixProd
            preFixProd *= nums[i] 
        
        for i in range(len(nums)-1, -1, -1):
            # Get the preFix product for each number, (product of all preceding numbers before each value non inclusive)
            res[i] *= postFixProd
            postFixProd *= nums[i] 
        
        return res