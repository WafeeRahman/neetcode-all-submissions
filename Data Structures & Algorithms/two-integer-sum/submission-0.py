class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSet = {}
        for i in range(len(nums)):
            if target - nums[i] in numSet:
                return [numSet[target-nums[i]], i]
            numSet[nums[i]] = i
        return [-1,-1] 
