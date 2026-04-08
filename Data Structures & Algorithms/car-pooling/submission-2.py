class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        minHeap = []
        for numP, fromi, toi in trips:
            dist = toi - fromi
            heapq.heappush(minHeap, [fromi, toi, numP])
        totalP = 0
        inCar = deque([])
        i = trips[0][1]
        print(minHeap)
        
        while minHeap or inCar:
            while inCar and i == inCar[0][1]:
                totalP -= inCar.popleft()[2]            
            
            while minHeap and i == minHeap[0][0]:
                newTrip = heapq.heappop(minHeap)
                totalP += newTrip[2] 
                if totalP > capacity:
                    return False
                
                inCar.append(newTrip)


            if minHeap and inCar:
                i = min(minHeap[0][0], inCar[0][1])
            elif minHeap and not inCar:
                i = minHeap[0][0]
            elif inCar:
                i = inCar[0][1]
        return True

                

            
        