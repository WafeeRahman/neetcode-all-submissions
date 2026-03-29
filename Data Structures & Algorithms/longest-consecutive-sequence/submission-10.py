class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0
        i = 0
        for i in range(len(nums)):
            #beginning of a sequence
            if (nums[i] - 1) not in numsSet: 
                val, count = nums[i], 0
                while val in numsSet:
                    val+=1
                    count+=1
                    print(val, count)
                longest = max(longest, count)
        return longest
        