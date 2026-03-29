class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for srz, dsz, cost in flights:
            adj[srz].append((dsz, cost))
        print(adj)


        #find the shortest path at lowest cost from src to dst, while not counting them as "stops"
        

        minHeap = [[0, src, k+1]] #Cost, Airport
        shortest = {}
        while minHeap:
            cost, dest, stops = heapq.heappop(minHeap)
            if dest == dst:
                return cost
            
            shortest[(dest, k)] = cost
    
            
            if stops > 0:
                for nei in adj[dest]:
                    if (nei[0], stops-1) not in shortest:
                        heapq.heappush(minHeap, [(cost+nei[1]), nei[0], stops-1])
        
        return -1      


        return shortest
        




