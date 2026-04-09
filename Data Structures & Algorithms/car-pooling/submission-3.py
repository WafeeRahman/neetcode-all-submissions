class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        trips.sort(key=lambda x:x[1])
        tripQ = deque(trips)
        curPassengers = 0
        tripHeap = []
        distance = tripQ[0][1]
        print(tripQ)
        while tripQ or tripHeap:
            
          


            while tripHeap and distance == tripHeap[0][0]:
                ti, poppedpassengers, fi = heapq.heappop(tripHeap)       
                curPassengers -= poppedpassengers
            
            while tripQ and distance == tripQ[0][1]:
                passengers, fromi, toi = tripQ.popleft()
                curPassengers += passengers
                if curPassengers > capacity:
                    return False
                heapq.heappush(tripHeap, [toi, passengers, fromi])
            
            if tripQ and tripHeap:
                nextLoc = min(tripQ[0][1], tripHeap[0][0])
            elif tripQ:
                nextLoc = tripQ[0][1]
            elif tripHeap:
                 nextLoc = tripHeap[0][0]

            distance = nextLoc
        
        return True
            

        