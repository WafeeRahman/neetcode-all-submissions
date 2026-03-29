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
                     
        i=0
        n = len(intervals)-1
        
        #Add All Non Overlapping Intervals that would occur before newInterval 
        while i <= n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i+=1
        
        #If we can merge down newInterval on an existing interval, continue merging the intervals
        #Until all succeeding intervals after the first merge are merged
        #Merging newinterval into existing cells will ensure we dont overshoot i,e [6,7], [9,10]
        while i <= n and newInterval[1] >= intervals[i][0]:
            #Merge Down New Interval
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i+=1
        merged.append(newInterval)

        #Merge any elements in the rest of the array after adding newinterval if req'd
        while i <= n:
            merged.append(intervals[i])
            i+=1
                         
        return merged
            
            
            