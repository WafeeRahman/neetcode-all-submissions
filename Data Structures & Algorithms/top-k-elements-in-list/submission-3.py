class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}
        buckets= [[] for i in range(len(nums)+1)]
        res = []
        
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for key in counts.keys():
            print(
                counts[key], key, buckets
            )
            buckets[counts[key]].append(key)
        

        for i in range(len(buckets)-1, -1,-1):
            if not(buckets[i]):
                continue
            for j in range(len(buckets[i])):
                if len(res) == k:
                    return res
                res.append(buckets[i][j])
        
        return res
        
        
            