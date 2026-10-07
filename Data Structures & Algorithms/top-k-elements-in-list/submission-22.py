class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        freq = [[] for _ in range (len(nums)+1)]
        for key, v in counts.items():
            freq[v].append(key)
        res = []
        for i in range(len(freq) -1, -1, -1):
            for val in freq[i]:
                res.append(val)
                if len(res) == k:
                    return res
    