class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0
        i = 0
        for i in range(len(nums)):
            #beginning of a sequence
            if (nums[i] - 1) not in numsSet: 
                count= 0
                while nums[i]+count in numsSet:
                    count+=1
                longest = max(longest, count)
        return longest
        