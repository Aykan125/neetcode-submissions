class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        adj = defaultdict(list)
        for i in range(len(points)):
            for j in range(i, len(points)):
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                cost = abs(x1-x2) + abs(y1-y2)

                adj[(x1,y1)].append((cost, x2, y2))
                adj[(x2,y2)].append((cost, x1, y1))
        visit = set()
        minHeap = []
        heapq.heapify(minHeap)
        heapq.heappush(minHeap, (0, points[0][0], points[0][1]))
        cost = 0
        while minHeap:
            if len(visit) == len(points):
                return cost
            temp, x, y = heapq.heappop(minHeap)
            if (x,y) in visit:
                continue
            visit.add((x,y))
            cost+=temp
            for c, x2, y2 in adj[(x,y)]:
                if (x2,y2) in visit:
                    continue
                heapq.heappush(minHeap,(c, x2, y2))
        return cost
                




        