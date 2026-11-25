class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = []
        minHeap.append((grid[0][0], 0, 0))
        visit = set()
        # visit.add((0,0))
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        while minHeap:
            time, r, c = heapq.heappop(minHeap)
            if (r, c) in visit:
                continue
            visit.add((r, c))
            if r==len(grid)-1 and c == len(grid) - 1:
                return time
            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if nr<0 or nc<0 or nr>=len(grid) or nc>=len(grid[0]) or (nr, nc) in visit:
                    continue
                heapq.heappush(minHeap, (max(time, grid[nr][nc]), nr, nc))
        return 0
            

            
        