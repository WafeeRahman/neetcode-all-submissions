class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        newArr = [0] * (2*n)

        for i in range(2*n):
            if i >= n:
                newArr[i] = nums[i%n]
            else:
                newArr[i] = nums[i]
        return newArr

        