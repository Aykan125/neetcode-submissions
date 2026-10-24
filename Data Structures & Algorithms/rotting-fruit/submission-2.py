class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #keeping multi bfsing until q empty
        #when q empty do a final pass to see if any 1's remaining if so remove

        q = deque()
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))

        def addFruit(r, c):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c] == 0 or grid[r][c] == 2:
                return
            grid[r][c] = 2
            q.append((r, c))
        minutes = -1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                addFruit(r+1,c)
                addFruit(r-1,c)
                addFruit(r,c+1)
                addFruit(r,c-1)
            minutes+=1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        if minutes<0:
            return 0
        return minutes