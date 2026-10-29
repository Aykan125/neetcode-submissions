class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort()
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output

        # for i, (start, end) in enumerate(intervals):
        #     if i+1 < len(intervals):
        #         if end < intervals[i+1][0]:
        #             res.append([start, end])
        #             continue
        #         else:
        #             # res.append([min(start, intervals[i+1][0]), max(end, intervals[i+1][1])])
        #             intervals[i+1][0] = min(start, intervals[i+1][0])
        #             intervals[i+1][1] = max(end, intervals[i+1][1])
        # res.append(intervals[-1])
        # return res
            
        