class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        projects = list(zip(capital, profits))
        heapq.heapify(projects)
        profit = w
        p = 0
        maxProfitHeap = []
        for p in range(k):
          
            while projects and projects[0][0] <= w:
                node = heapq.heappop(projects)
                heapq.heappush(maxProfitHeap, [-node[1], node[0]])
            
            if maxProfitHeap:
                optimalProject = heapq.heappop(maxProfitHeap)
                profit += -optimalProject[0]
                w +=  -optimalProject[0]

        return profit
            




