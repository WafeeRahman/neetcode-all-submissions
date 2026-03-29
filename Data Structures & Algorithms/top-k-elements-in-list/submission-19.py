class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range (len(nums) + 1)]

        countMap = defaultdict(int)

        for i in range(len(nums)):
            countMap[nums[i]] += 1
        
        for key in countMap:
            buckets[countMap[key]].append(key)
        
        res = []
        for i in range(len(buckets)-1, -1, -1):
            for j in range(len(buckets[i])):
                if len(res) == k:
                    return res
                res.append(buckets[i][j])
                
        return res[:k+1]
            


