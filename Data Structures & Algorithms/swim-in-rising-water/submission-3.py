class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        minHeap = [(grid[0][0], 0,0)]
        visit = set()
        directions=[[0,-1],[-1,0],[1,0],[0,1]]
        while minHeap:
            d, r, c = heapq.heappop(minHeap)
            if r==N-1 and c == N-1:
                return d
            if (r,c) in visit:
                continue
            visit.add((r,c))
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if (nr,nc) in visit or nr<0 or nr>=N or nc<0 or nc>=N:
                    continue
                heapq.heappush(minHeap, (max(d, grid[nr][nc]), nr, nc))
            


        