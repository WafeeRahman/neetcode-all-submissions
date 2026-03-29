class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        
        #Turn the Number Stream into a MinHeap
        heapq.heapify(self.heap)
        
        #We only need a stream of >= K Values, so pop the MinHeap until we have K values, so we can
        #Get The Result In O(1) Time
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        



        
        

    def add(self, val: int) -> int:
        
        #Push into heap and percolate up
        heapq.heappush(self.heap, val)
        
        #Remove Until We Have K Values Again if Necessary
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        #KTH Largest in a min-heap is the len(Heap) - k
        return self.heap[len(self.heap)-self.k]




        
