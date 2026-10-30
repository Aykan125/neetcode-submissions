class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                if board[r][c] in row[r]:
                    return False
                else:
                    row[r].add(board[r][c])
                if board[r][c] in col[c]:
                    return False
                else:
                    col[c].add(board[r][c])
                if board[r][c] in square[(r//3, c//3)]:
                    return False
                else:
                    square[(r//3, c//3)].add(board[r][c])
        return True
        

        