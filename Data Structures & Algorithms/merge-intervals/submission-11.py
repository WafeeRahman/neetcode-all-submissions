#Given an array of intervals where inteverals[i] = [starti, endi] merge all intervals that overlap
#Return the merged array after merging all overlapping intervals
#Intervals overlap if the start of the next interval is equal to the end of the last
#Or if the start of one interval is equal to the last
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prevInterval = None
        merged = []

        for i in range(len(intervals)):
          
            if not merged:
                merged.append(intervals[i])
                continue
            currInterval = intervals[i]
            prevInterval = merged[-1]
            print(currInterval, prevInterval)
            #Check if the intervals overlap ()
            #If the previous interval has the same or greater start as the current interval
            #Interval s.t currEnd >= prevStart >= prevBeginning
         
            
            #When the end of the last interval is >= to the beginning, there are no gurantees if
            #The end of the current interval <= the end of the previous interval
            #Therefore, the start of the merged interval should be the minimum
            #Of the two starting intervals, and the end should be the maximum of the two endings
            if prevInterval[1] >= currInterval[0]:
                merged.pop()
                merged_start = min(prevInterval[0], currInterval[0])
                merged_end = max(prevInterval[1], currInterval[1])
                merged.append([merged_start, merged_end])
            else:
                merged.append(currInterval)
        return merged
            

        