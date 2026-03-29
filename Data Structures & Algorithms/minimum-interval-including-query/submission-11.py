#Given a 2D Integer array of intervals
#We have an array of queries, where in each query we need to find the length of the shortest interval
#Such that the interval start <= query <= intervals end
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        #Sort by Size
        intervals.sort(key=lambda x: x[0])
        minHeap = []
        contiguousQueries = queries.copy()
        queries.sort()
        queryMap = {}
        j = 0
        for i in range(len(queries)):
          
 
            while j < len(intervals) and intervals[j][0] <= queries[i]:
                heapq.heappush(minHeap, [((intervals[j][1]-intervals[j][0])+1),intervals[j][0], intervals[j][1]])
                j+=1
            
            while minHeap and minHeap[0][2] < queries[i]:
                heapq.heappop(minHeap)

            if minHeap:
                queryMap[queries[i]] = minHeap[0][0]
            else:
                queryMap[queries[i]] = -1
            
            
        return [queryMap[q] for q in contiguousQueries]
      
                


                    
           



        