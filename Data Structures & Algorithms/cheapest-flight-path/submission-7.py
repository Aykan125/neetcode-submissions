class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for source, destination, price in flights:
            adj[source].append((price, destination))
        minHeap = []
        visit = set()
        minHeap.append((0, 0, src))
        minStops = [float("INF")]*n

        while minHeap:
            price, stops, node = heapq.heappop(minHeap)
            if stops-1 > k:
                continue
            if stops > minStops[node]:
                continue
            minStops[node]= stops
            if stops-1<=k and node == dst:
                return price
            for p2, d2 in adj[node]:
                heapq.heappush(minHeap, (price+p2, stops+1, d2))
        return -1
            
            
        