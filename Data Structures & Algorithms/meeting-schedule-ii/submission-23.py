"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
#Given a list of meetuing room intervals, calculate the minimum number of days to schedule meetings with no conflicts
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #The amount of conflicts we have in a single day is indicated by the amount of overlaps we 
        #Have with the minimum ending within all intervals and the start of each interval

        #Populate stream of minui
        minHeap = []
        #Sort by starting
        intervals.sort(key=lambda x: x.start)

        for interval in intervals:
            if minHeap and minHeap[0] <= interval.start:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, interval.end)
        return len(minHeap)
            

        