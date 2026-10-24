class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, visit, prevHeight):
            if r<0 or c<0 or c>=COLS or r >= ROWS or heights[r][c]<prevHeight or (r,c) in visit:
                return
            visit.add((r,c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, -1)
            dfs(ROWS-1, c, atl, -1)
        for r in range(ROWS):
            dfs(r, 0, pac, -1)
            dfs(r, COLS-1, atl, -1)
        res = []
        for r, c in pac:
            if (r,c) in atl:
                res.append([r, c])
        return res

        