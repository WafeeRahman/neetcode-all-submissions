class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-num for num in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            print(maxHeap)
            x = -(heapq.heappop(maxHeap))
            y = -(maxHeap[0])
            print(x,y, maxHeap)
            
            if x == y: 
                heapq.heappop(maxHeap)
            else:
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, -(abs(y-x)))

        return abs(maxHeap[0]) if len(maxHeap) > 0 else 0

        