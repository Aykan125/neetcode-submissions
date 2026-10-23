class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()

        string = []
        def dfs(row, col):
            if len(string) == len(word):
                if "".join(string) == word:
                    return True
                return False
            if row>=rows or col >=cols or row < 0 or col < 0 or (row,col) in path:
                return False

            string.append(board[row][col])
            path.add((row,col))

            decision = dfs(row+1, col) or dfs(row-1, col) or dfs(row, col+1) or dfs(row, col-1)
            path.remove((row,col))
            string.pop()

            return decision
        for i in range(rows):
            for j in range(cols):
                if dfs(i,j):
                    return True
        return False




        