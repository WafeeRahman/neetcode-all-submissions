#With an array of nonoverlapping intervals sorted in ascending order, we're giving a new interval to insert
#into intervals such that intervals is still sorted in ascending order and also intervals still does not have
#Any overlapping intervals

#Approach, find an interval within arr where
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        flag = True
        #2 Conditions -> newInterval doesnt overlap with anyone
                         #newInterval overlaps with a value and we need to remerge the entire array
                         #A value overlaps with curinterval and we need to remerge the entire array
        i=0
        n = len(intervals)-1
        
        #Add All Non Overlapping Intervals
        while i <= n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i+=1
        
        while i <= n and newInterval[1] >= intervals[i][0]:
            #Merge Down New Interval
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i+=1

        merged.append(newInterval)
            
        while i <= n:
            if merged[-1][1] >= intervals[i][0]:
                merged[-1][1] = max(merged[-1][1], intervals[i][-1])
            else:
                merged.append(intervals[i])
            i+=1
                         
        return merged
            
            
            