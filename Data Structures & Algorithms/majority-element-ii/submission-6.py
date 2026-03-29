class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        for i in range(len(nums)):
            freq[nums[i]] += 1
        res = []
        for key in freq:
            if freq[key] > len(nums) // 3:
                res.append(key)
        return res
        

        