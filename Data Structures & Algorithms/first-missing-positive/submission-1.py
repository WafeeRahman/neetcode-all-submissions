class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        nums = set(nums)

        minOfNums = min(nums)
        if minOfNums > 1:
            return 1
        count = 0

        while True:
            if minOfNums+count not in nums and minOfNums+count > 0:
                return minOfNums+count
            count+=1
        