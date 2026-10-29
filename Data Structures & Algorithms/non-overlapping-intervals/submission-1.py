class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = float("-INF")
        res = 0

        for start, end in intervals:
            if start>=prevEnd:
                prevEnd = end
            else:
                prevEnd = min(end, prevEnd)
                res+=1
        return res
        