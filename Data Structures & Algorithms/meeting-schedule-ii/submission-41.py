"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        minHeap = []

        for i in sorted(intervals, key= lambda x: x.start):
            if minHeap and i.start >= minHeap[0]:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, i.end)
        
        return len(minHeap)