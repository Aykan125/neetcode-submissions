class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for i in range(n)] for _ in range(n)]
        posDiag = set()
        negDiag = set()
        col = set()
        output = []

        def dfs(r):
            if r == n:
                output.append(["".join(board[k]) for k in range(n)])
                return
            for c in range(n):
                if c in col or r + c in posDiag or r-c in negDiag:
                    continue
                posDiag.add(r+c)
                negDiag.add(r-c)
                col.add(c)
                board[r][c] = "Q"
                dfs(r+1)
                board[r][c] = "."
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                col.remove(c)
        dfs(0)
        return output

        