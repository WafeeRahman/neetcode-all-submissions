class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in indexes:
                return [indexes[diff], i]
            if nums[i] not in indexes:
                indexes[nums[i]] = i
        return [-1,-1]