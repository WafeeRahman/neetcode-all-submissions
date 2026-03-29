class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}
        minHeap = []
        res = []
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for key in counts.keys():
            minHeap.append([counts[key], key])
        
        heapq.heapify(minHeap)

        while len(minHeap) > k:
            heapq.heappop(minHeap)
        
        for i in range(len(minHeap)):
            res.append(minHeap[i][1])
        
        return res
            