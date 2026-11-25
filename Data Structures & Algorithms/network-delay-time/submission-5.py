class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for source, target, time in times:
            adj[source].append((time, target))
        visit = set()
        minHeap = []
        minHeap.append((0, k))
        heapq.heapify(minHeap)
        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            if len(visit) == n:
                return time
            for t, nei in adj[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, (time+t, nei))
        return -1
            

        