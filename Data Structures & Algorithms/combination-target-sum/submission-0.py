class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        subSet = []
        subSum = 0
       
       
        def BackTrack(i, nums):
            nonlocal subSum, res, subSet
            if i >= len(nums) or subSum >= target:
                print(subSet, subSum)
                if subSum == target:
                    res.append(subSet[:])
                return

            if subSum <= target:
                subSum += nums[i]
                subSet.append(nums[i])
            
            BackTrack(i, nums)
            
            subSum -= nums[i]
            subSet.pop()
            
            BackTrack(i+1, nums)
        
        BackTrack(0, nums)

        return res
            







        