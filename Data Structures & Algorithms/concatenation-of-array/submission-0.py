class Solution:
    #Given an array, create a funtion that concatenates it ones, creating an array of length 2n, where n is the og length

    def getConcatenation(self, nums: List[int]) -> List[int]:

        res = [0] * (2 * len(nums))

        for i in range(len(nums)):
            res[i] = nums[i]
            res[i+len(nums)] = nums[i]
        
        return res 
        