class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for src2, dst2, cost in flights:
            adj[src2].append((cost, dst2, float("INF")))

        minHeap = [(0, src, 0)]
        #visit = set()

        while minHeap:
            cost, node, stops = heapq.heappop(minHeap)
            if node == dst and (stops - 1)<=k:
                return cost
            if stops>k:
                continue
            for i, (edgeWeight, nei, neiStops) in enumerate(adj[node]):
                if stops + 1 < neiStops:
                    heapq.heappush(minHeap, (edgeWeight+cost, nei, stops+1))
                    adj[node][i] = (edgeWeight, nei, stops+1)
        return -1



        