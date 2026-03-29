class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for srz, dsz, cost in flights:
            adj[srz].append((dsz, cost))
        print(adj)


        #find the shortest path at lowest cost from src to dst, while not counting them as "stops"
        

        minHeap = [[0, src, k+1]] 
        dist = {} #Min Cost at (destination, stops remaining)
        
        while minHeap:
            cost, dest, stops = heapq.heappop(minHeap)
            if dest == dst:
                return cost
            dist[(dest, stops)] = cost
            #If we can make more stops, add more flights
            if stops > 0:
                for nei in adj[dest]:
                    newCost = cost+nei[1]
                    if (nei[0], stops-1) not in dist:
                        heapq.heappush(minHeap, [newCost, nei[0], stops-1])
            


      
        return -1      


        




