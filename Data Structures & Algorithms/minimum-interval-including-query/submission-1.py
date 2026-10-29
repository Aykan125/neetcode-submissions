class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []
        mapping = {}
        ptr = 0

        for i in sorted(queries):
            while ptr<len(intervals) and intervals[ptr][0] <= i:
                l, r = intervals[ptr]
                ptr+=1
                heapq.heappush(minHeap, (r-l+1, r))
            while minHeap and minHeap[0][1] <i:
                heapq.heappop(minHeap)
            mapping[i] = minHeap[0][0] if minHeap else -1
        return [mapping[i] for i in queries]



        