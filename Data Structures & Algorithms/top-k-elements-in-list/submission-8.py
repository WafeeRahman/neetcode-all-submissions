class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        numCounts = [[v,k] for k,v in counts.items()]
        
        minheap = numCounts 
        heapq.heapify(minheap)
        
        while len(minheap) > k:
            heapq.heappop(minheap)
        
        res = []
        for i in range(k):
            res.append(minheap[i][1])

        return res    
        