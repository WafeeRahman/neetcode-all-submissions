class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countMap = defaultdict(int)
        n = len(nums)

        for i in range(len(nums)):
            countMap[nums[i]] += 1

            if countMap[nums[i]] > int(n/2):
                return nums[i]

    