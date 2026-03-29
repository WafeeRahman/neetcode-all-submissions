#Given a 2D Integer array of intervals
#We have an array of queries, where in each query we need to find the length of the shortest interval
#Such that the interval start <= query <= intervals end
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        #Sort by Size
        intervals.sort(key=lambda x: ((x[1] - x[0])+1))
        print(intervals)
        print(queries)
        minHeap = []
        res = []
        for i in range(len(queries)):
            
            for j in range(len(intervals)):
                if intervals[j][0] <= queries[i] <= intervals[j][1]:

                    print(intervals[j])
                    res.append((intervals[j][1] - intervals[j][0]) + 1)
                    break
            if len(res) < i+1:
                res.append(-1)
                continue
        return res


        