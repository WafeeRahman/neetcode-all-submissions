class MedianFinder:

    def __init__(self):
        self.minHeap = [] #minheap of maxes
        self.maxHeap = [] #maxheap of mins
 
        

    def addNum(self, num: int) -> None:
    
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        
        if abs(len(self.minHeap) - len(self.maxHeap)) > 1:
            A, B = self.minHeap, self.maxHeap
            if len(A) < len(B):
                A, B = B,A
            val = heapq.heappop(A)
            heapq.heappush(B, -val)
    
    def findMedian(self) -> float:
        total = len(self.minHeap) + len(self.maxHeap)
        if total % 2:
            if len(self.minHeap) > len(self.maxHeap):
                val= self.minHeap[0]
            else:
                val= -self.maxHeap[0]
            return val
        else:
            val1 = self.minHeap[0]
            val2 = self.maxHeap[0]
            val2 = -val2

            return (val1+val2) / 2

        
        