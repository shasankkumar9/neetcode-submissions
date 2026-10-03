"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # minHeap = []

        # for i in sorted(intervals, key= lambda x: x.start):
        #     if minHeap and i.start >= minHeap[0]:
        #         heapq.heappop(minHeap)
        #     heapq.heappush(minHeap, i.end)
        
        # return len(minHeap)

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