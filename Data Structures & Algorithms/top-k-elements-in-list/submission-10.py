class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range (len(nums) + 1)]
        counts = defaultdict(int)
        
        for num in nums:
            counts[num] += 1

        for key in counts:
            occ = counts[key]
            freq[occ].append(key)

        res = []
        
        for i in range(len(freq)):
            if not freq[i]:
                continue
            for j in range(len(freq[i])):
                res.append(freq[i][j])

        return res[len(res) - k:]
        


      