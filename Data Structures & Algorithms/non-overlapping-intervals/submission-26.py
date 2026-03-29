#Given an array of intervals where intervals[i] = [si, ei], return the number of intervals yhou need to remove
#Such that all of the intervals are nonoverlapping
#Overlapping intervals are intervals where the end of one interval > the start of the next

#[[1,2],[2,4],[1,4]] [2,4] over laps with [1,4]
#Aswell as [1,2] overlapping with [1,4], if we removed [1,4] the intervals would no longer be overlapping
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[1])
        print(intervals)

        remove = 0
        remove2 = 0
        l = 0
        maxEnd = [float('-inf'), float('-inf')]
        for r in range(len(intervals)):
            if maxEnd[1] > intervals[r][0]:
                remove2 += 1
                continue
            
            if intervals[r][1] > maxEnd[1] and intervals[r][0] > maxEnd[0]:
                maxEnd = intervals[r]
            
            elif intervals[r][1] > maxEnd[1] and intervals[r][0] <= maxEnd[0]:
                remove2+=1
        
        return remove2

        