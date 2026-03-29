class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    #We can use prefixes to take the product of each value except itself
    #The product would be the prefix product of the left value, multiplied by the prefix product of the right value
    #Where the right value prefix starts from the right
    #For each ith position
        res = [0] * len(nums)

        prefix = 1
        postfix = 1

        for i in range(len(nums)):
            res[i] = prefix 
            prefix = prefix * nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res