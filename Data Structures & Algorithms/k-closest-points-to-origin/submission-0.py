class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        for point in points:
            x, y = point[0], point[1]
            distance = math.sqrt((x-0)**2 + (y-0)**2)
            heapq.heappush(minHeap, [distance, x, y])
        while len(res) < k:
            point = heapq.heappop(minHeap)
            res.append(point[1:])
        return res
        