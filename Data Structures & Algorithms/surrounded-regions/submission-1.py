class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        unsurrounded = set()
        def dfs(r, c):
            if r<0 or c<0 or r>=ROWS or c >= COLS or (r,c) in unsurrounded or board[r][c] == "X":
                return
            unsurrounded.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for c in range(COLS):
            print(ROWS-1, c)
            print(unsurrounded)
            if board[0][c] == "O" and (0,c) not in unsurrounded:
                dfs(0, c)
            if board[ROWS-1][c] == "O" and (ROWS-1,c) not in unsurrounded:
                dfs(ROWS-1, c)
        for r in range(ROWS):
            if board[r][0] == "O" and (r,0) not in unsurrounded:
                dfs(r, 0)
            if board[r][COLS-1] == "O" and (r,COLS-1) not in unsurrounded:
                dfs(r, COLS-1)

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in unsurrounded:
                    continue
                board[r][c] = "X"

        print(unsurrounded)
        
            

        