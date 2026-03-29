class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNums = {}
        for num in nums:
            countNums[num] = countNums.get(num, 0) + 1
        sortedNums = sorted(countNums.keys(), key=lambda x: countNums[x])
        return sortedNums[::-1][:k]