class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []

        for x,y in points:
            dist = math.sqrt((x-0)**2 + (y-0)**2)
            heapq.heappush(minHeap, (-dist,x,y))
        
        while len(minHeap) > k:
            heapq.heappop(minHeap)
        
        return [[x,y] for dist,x,y in minHeap]