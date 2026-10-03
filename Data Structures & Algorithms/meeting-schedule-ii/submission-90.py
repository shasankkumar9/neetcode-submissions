"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        mh = []

        for i in sorted(intervals, key= lambda x: x.start):
            if mh and mh[0] <= i.start:
                heapq.heappop(mh)
            heapq.heappush(mh, i.end)
        
        return len(mh)