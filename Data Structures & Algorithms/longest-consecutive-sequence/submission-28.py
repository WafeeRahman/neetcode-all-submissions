class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for i in range(len(nums)):
            j=0
            if nums[i] - 1 not in numSet:
                while j + nums[i] in numSet:
                    j+=1
                res = max(res, j)
        return res