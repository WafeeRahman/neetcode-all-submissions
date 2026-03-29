class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        maxCount = 0
        for i in range(len(nums)):
            if not (nums[i] - 1 in numSet):
                count = 0
                while nums[i] + count in numSet:
                    count+=1
                maxCount = max(count, maxCount)
        return maxCount

        
        