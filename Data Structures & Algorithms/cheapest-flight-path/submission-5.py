class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []

        for srz, dsz, cost in flights:
            adj[srz].append((dsz, cost))

        #Apply Djikstras to find the shortest minimum costing path while maintaining that the DST is met within k stops

        minHeap = [[0, src, k+1]]
        ticketSet = {}

        while minHeap:
            cost, dest, stopsRemaining = heapq.heappop(minHeap)
            if dest == dst:
                return cost
            
            ticketSet[(dest, stopsRemaining)] = cost
            
            if stopsRemaining > 0:
                for nei in adj[dest]:
                    if (nei[0], stopsRemaining-1) not in ticketSet:
                        heapq.heappush(minHeap, [(cost+nei[1]), nei[0], stopsRemaining-1])
        return -1 