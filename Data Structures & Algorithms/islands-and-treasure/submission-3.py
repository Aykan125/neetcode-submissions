class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        dist = 0
        def addRoom(q, r, c):
            if r<0 or c<0 or c>=cols or r>=rows or grid[r][c] != 2147483647:
                return
            grid[r][c] = dist+1
            q.append((r,c))
        while q:
            for i in range(len(q)):
                row, col= q.popleft()
                addRoom(q,row+1,col)
                addRoom(q,row-1,col)
                addRoom(q,row,col+1)
                addRoom(q,row,col-1)
            dist+=1
        

            
        