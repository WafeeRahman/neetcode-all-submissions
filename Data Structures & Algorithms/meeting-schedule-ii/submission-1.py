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
        curDay = intervals
        days = 0
        while curDay:

            i = 1
            prevEnd = curDay[0].end
            nextDay = []
            while i < len(curDay):
                while i < len(curDay) and prevEnd > curDay[i].start:
                    nextDay.append(curDay[i])
                    i+=1
                if i < len(curDay):
                    prevEnd = curDay[i].end
                i+=1
            days += 1
            curDay = nextDay
        return days

                
                
