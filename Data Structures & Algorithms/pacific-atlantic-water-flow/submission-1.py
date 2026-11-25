class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacSet = set()
        atSet = set()

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, prevHeight, curSet):
            if r<0 or c<0 or r>=rows or c>= cols or heights[r][c]<prevHeight or (r, c) in curSet:
                return
            curSet.add((r,c))
            dfs(r+1, c, heights[r][c], curSet)
            dfs(r-1, c, heights[r][c], curSet)
            dfs(r, c+1, heights[r][c], curSet)
            dfs(r, c-1, heights[r][c], curSet)

            return
        for r in range(rows):
            if (r, 0) not in pacSet:
                dfs(r, 0, 0, pacSet)
            if (r, cols-1) not in atSet:
                dfs(r, cols-1, 0, atSet)
        for c in range(cols):
            if (0, c) not in pacSet:
                dfs(0, c, 0, pacSet)
            if (rows-1, c) not in atSet:
                dfs(rows-1, c, 0, atSet)
        output = []
        for r, c in pacSet:
            if (r, c) in atSet:
                output.append([r, c])
        return output

            
                
        