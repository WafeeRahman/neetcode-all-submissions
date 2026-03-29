class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        minHeap = []
        for num in nums:
            count[num] = count.get(num, 0 ) + 1

        for key in count:
            heapq.heappush(minHeap, [count[key], key])

        while len(minHeap) > k:
            heapq.heappop(minHeap)
        
        return [arr[1] for arr in minHeap]
        
        