class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
        minutes = -1
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if nr<0 or nc<0 or nr>=rows or nc>=cols or grid[nr][nc]!=1:
                        continue
                    grid[nr][nc] = 2
                    q.append((nr, nc))
            minutes+=1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return minutes if minutes!=-1 else 0


                    

        