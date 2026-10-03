"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        # mh = []

        # for i in sorted(intervals, key= lambda x: x.start):
        #     if mh and mh[0] <= i.start:
        #         heapq.heappop(mh)
        #     heapq.heappush(mh, i.end)
    
        # return len(mh)

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res = 0
        j = 0
        for i in range(len(intervals)):
            if start[i] < end[j]:
                res += 1
            else:
                j += 1
        
        return res