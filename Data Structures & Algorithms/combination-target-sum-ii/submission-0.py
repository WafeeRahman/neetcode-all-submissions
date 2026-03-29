class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        res = []
        subset = []
        subSum = 0 

        def BackTrack(i, nums):
            nonlocal res, subset, subSum
            
            if i >= len(nums) or subSum >= target:
                print(subset, subSum)
                if subSum == target:
                    res.append(subset[:])
                return
            
            if subSum <= target:
                subSum += nums[i]
                subset.append(nums[i])
                
            
            BackTrack(i+1, nums)
            subSum -= nums[i]
            subset.pop()
            if subSum + nums[i] > target:
                return
            
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i+=1
            BackTrack(i+1, nums)
            
        
        BackTrack(0, nums)

        return res
