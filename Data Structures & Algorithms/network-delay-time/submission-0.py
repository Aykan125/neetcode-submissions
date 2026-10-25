class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(n+1)}
        for u, v, t in times:
            adj[u].append((t,v))
        visit = set()
        w = 0
        minHeap = [(0,k)]
        heapq.heapify(minHeap)
        while minHeap:
            t, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            w = t
            for i in adj[node]:
                if i[1] not in visit:
                    heapq.heappush(minHeap, (t+i[0], i[1]))
        return w if len(visit) == n else -1
            


        