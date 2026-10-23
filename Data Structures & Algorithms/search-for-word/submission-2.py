class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()

        string = []
        def dfs(i, row, col):
            if i == len(word):
                return True
            # return False
            if row>=rows or col >=cols or row < 0 or col < 0 or board[row][col] == "#" or word[i]!=board[row][col]:
                return False
            
            # path.add((row,col))
            board[row][col] = "#"

            decision = dfs(i+1,row+1, col) or dfs(i+1,row-1, col) or dfs(i+1,row, col+1) or dfs(i+1,row, col-1)
            board[row][col] = word[i]
            # path.remove((row,col))

            return decision
        for i in range(rows):
            for j in range(cols):
                if dfs(0,i,j):
                    return True
        return False




        