class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        val = nums[0]

        for num in nums[1:]:
            val = val ^ num
        return val