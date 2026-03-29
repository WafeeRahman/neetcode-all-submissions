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
            #Check if the intervals overlap ()
            if prevInterval[0] >= currInterval[0]:
                merged.pop()
                merged.append([prevInterval[0], currInterval[1]])
            elif prevInterval[1] >= currInterval[0]:
                merged.pop()
                merged_start = min(prevInterval[0], currInterval[0])
                merged_end = max(prevInterval[1], currInterval[1])
                merged.append([merged_start, merged_end])
            else:
                merged.append(currInterval)
        return merged
            

        