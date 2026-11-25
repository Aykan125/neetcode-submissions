class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                mDist = abs(x1-x2) + abs(y1-y2)
                adj[(x1, y1)].append((mDist, x2, y2))
                adj[(x2, y2)].append((mDist, x1, y1))
        res = 0
        visit = set()
        minHeap = []
        minHeap.append((0, points[0][0], points[0][1]))
        while minHeap:
            dist, x1, y1 = heapq.heappop(minHeap)
            if (x1, y1) in visit:
                continue
            visit.add((x1, y1))
            res+=dist
            if len(visit) == len(points):
                return res
            for d, x2, y2 in adj[(x1, y1)]:
                if (x2, y2) not in visit:
                    heapq.heappush(minHeap, (d, x2, y2))
        return res


        