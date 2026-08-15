class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        minHeap = []
        intervals.sort(key=lambda x:x[0])
        res = [-1 for _ in range(len(queries))]
        for i in range(len(queries)):
            queries[i] = [queries[i], i]
        qCopy = sorted(queries, key=lambda x:x[0])
        
        i = 0
        for query in qCopy:
            
        
            #Add all valid values that lefti <= queries[j]
            while i < len(intervals) and intervals[i][0] <= query[0]:
                heapq.heappush(minHeap, ((intervals[i][1] -intervals[i][0])+1, intervals[i][1]))
                i+=1
            
            #Popout Invalid Values and get minLen
            while minHeap and minHeap[0][1] < query[0]:
                intLen, endVal = heapq.heappop(minHeap)
            maxLen = minHeap[0][0] if minHeap else -1
            res[query[1]] = maxLen
            
        return res

        