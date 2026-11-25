class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((0, r, c))
        directions = [(0,1), (0,-1), (1, 0), (-1, 0)]
        while q:
            for i in range(len(q)):
                dist, row, col = q.popleft()
                # grid[row][col] = dist
                for dr, dc in directions:
                    nr, nc = row + dr, col+dc
                    if nr>=rows or nc>=cols or nr<0 or nc<0 or grid[nr][nc]!=2147483647:
                        continue
                    grid[nr][nc] = dist+1
                    q.append((dist+1, nr, nc))
        
        