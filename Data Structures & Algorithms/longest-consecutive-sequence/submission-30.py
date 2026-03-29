class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums= set(nums)

       
        res = 0
        for num in nums:
            count = 0
            #beginning
            if num-1 not in setNums:
                while num + count in setNums:
                    count+=1
                    res = max(res, count)
        return res
        
        