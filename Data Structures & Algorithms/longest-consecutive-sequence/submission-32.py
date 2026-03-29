class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        count = 0
        largest = 0
        for num in nums:
            count = 0 
            if num-1 not in numSet:
                while num+count in numSet:
                    count+=1
                largest = max(count, largest)
        return largest