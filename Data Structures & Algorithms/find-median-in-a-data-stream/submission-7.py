class MedianFinder:

    def __init__(self):
        self.smallHeap = []
        self.largeHeap = []

    def addNum(self, num: int) -> None:
        if not self.smallHeap and not self.largeHeap:
            self.smallHeap.append(-num)
        else:
            if num <= abs(self.smallHeap[0]):
                heapq.heappush(self.smallHeap, -num)
            else:
                heapq.heappush(self.largeHeap, num)
            
            print(self.smallHeap, self.largeHeap)

            while abs(len(self.smallHeap) - len(self.largeHeap)) > 1:
                if len(self.smallHeap) > len(self.largeHeap):
                    x = heapq.heappop(self.smallHeap)
                    heapq.heappush(self.largeHeap, -x)
                
                elif len(self.largeHeap) > len(self.smallHeap):
                    x = heapq.heappop(self.largeHeap)
                    heapq.heappush(self.smallHeap, -x)
                
                else:
                    break
            print(self.smallHeap, self.largeHeap)

    def findMedian(self) -> float:
        if not self.smallHeap and not self.largeHeap:
            return None
        if len(self.smallHeap) == len(self.largeHeap):
            x = self.smallHeap[0]
            x = -x
            y = self.largeHeap[0]
            return (x+y)/2
        else:
            if len(self.smallHeap) > len(self.largeHeap):
                return -(self.smallHeap[0])
            else:
                return self.largeHeap[0]
            
        
        