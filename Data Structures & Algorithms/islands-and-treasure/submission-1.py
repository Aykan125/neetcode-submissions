class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c, 0))

        while q:
            row, col, dist = q.popleft()

            if (row < 0 or col < 0 or
                row >= rows or col >= cols or
                grid[row][col] == -1 or
                (grid[row][col] != 2147483647 and dist != 0)):
                continue

            q.append((row + 1, col, dist + 1))
            q.append((row - 1, col, dist + 1))
            q.append((row, col + 1, dist + 1))
            q.append((row, col - 1, dist + 1))

            if grid[row][col] == 2147483647:
                grid[row][col] = dist