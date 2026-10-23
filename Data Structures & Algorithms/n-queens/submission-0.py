class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        output = []
        board = [["."]*n for i in range(n)]
        col = set()
        posDiag = set()
        negDiag = set()

        def dfs(r):
            if r>=n:
                output.append(["".join(row) for row in board])
                return
            for k in range(len(board[0])):
                if k in col or (r+k) in posDiag or (r-k) in negDiag:
                    continue
                col.add(k)
                posDiag.add(r+k)
                negDiag.add(r-k)
                board[r][k] = "Q"
                dfs(r+1)
                board[r][k] = "."
                col.remove(k)
                posDiag.remove(r+k)
                negDiag.remove(r-k)
        dfs(0)
        return output
        