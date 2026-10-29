class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort()
        res = []

        for i, (start, end) in enumerate(intervals):
            if i+1 < len(intervals):
                if end < intervals[i+1][0]:
                    res.append([start, end])
                    continue
                else:
                    # res.append([min(start, intervals[i+1][0]), max(end, intervals[i+1][1])])
                    intervals[i+1][0] = min(start, intervals[i+1][0])
                    intervals[i+1][1] = max(end, intervals[i+1][1])
        res.append(intervals[-1])
        
        if intervals[-1][0] > res[-1][1]:
            res.append(intervals[-1])
        return res
            
        