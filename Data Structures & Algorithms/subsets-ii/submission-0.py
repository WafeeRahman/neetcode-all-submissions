class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subSet = []

        def BackTrack(i):
            
            if i >= len(nums):
                res.append(subSet[:])
                return
            
            subSet.append(nums[i])
            
            BackTrack(i+1)
            
            subSet.pop()
            
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i+=1
            
            BackTrack(i+1)
            
        BackTrack(0)
        return res
            
            
