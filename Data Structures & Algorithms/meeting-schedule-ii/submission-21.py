"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

#Given an array of meeting time interval objects consisting of start and end times
#Find the minimum days to schedule all meetings without any conflicts

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start) #Sort by starting time
        if len(intervals) == 0:
            return 0
        minHeap = []

        maxCount = 0
        for i in range(len(intervals)):
            #If the maximum ended meeting does not overlap with the start, pop it
            if minHeap and minHeap[0] <= intervals[i].start:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, intervals[i].end)
        return len(minHeap)
            
                
                
