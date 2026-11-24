class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(i, r, c):
            if i == len(word):
                return True
            if r>=rows or c>=cols or c<0 or r<0 or (r, c) in path or word[i] != board[r][c]:
                return False

            path.add((r, c))
            
            decision = dfs(i+1, r+1, c) or dfs(i+1, r-1, c) or dfs(i+1, r, c+1) or dfs(i+1, r, c-1)

            path.remove((r, c))

            return decision

        for r in range(rows):
            for c in range(cols):
                if dfs(0, r, c):
                    return True
        return False
            
