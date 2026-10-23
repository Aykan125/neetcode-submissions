class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks)
        heap = [-c for c in count.values()]
        heapq.heapify(heap)
        q = deque()
        time = 0
        while heap or q:
            time+=1
            if heap:
                num = heapq.heappop(heap)
                num+=1
                if num:
                    q.append([num, time+ n])
            if q and q[0][1] == time:
                num = q.popleft()[0]
                heapq.heappush(heap, num)
        return time


        