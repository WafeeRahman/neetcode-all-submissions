class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        
        if abs(len(self.maxHeap) - len(self.minHeap)) > 1:
            A, B = self.maxHeap, self.minHeap
            if len(A) < len(B):
                A, B = B,A
            
            heapq.heappush(B, -heapq.heappop(A))
        
        

    def findMedian(self) -> float:

        total = len(self.minHeap) + len(self.maxHeap)
        if total % 2 == 1:
            if len(self.minHeap) > len(self.maxHeap):
                return self.minHeap[0]
            else:
                return -self.maxHeap[0]
        else:
            val1 = self.minHeap[0]
            val2 = -self.maxHeap[0]
            return (val1+val2)/2
        