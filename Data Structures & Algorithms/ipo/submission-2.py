class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        

        for i in range(len(capital)):
            capital[i] = [capital[i], profits[i]]
        
        heapq.heapify(capital)

        projects = []
        profit = w

        for p in range(k):

            while capital and capital[0][0] <= w:
                project = heapq.heappop(capital)
                heapq.heappush(projects, [-project[1], project[0]])
            if projects:
                optimalProject = heapq.heappop(projects)
                profit += -optimalProject[0]
                w += -optimalProject[0]
        return profit

