class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])
        
        def lookthrough(r, c):
            if r < 0 or c < 0 or c >= cols or r >= rows or board[r][c] != "O":
                return
            
            board[r][c] = "S"
            lookthrough(r - 1, c)
            lookthrough(r + 1, c)
            lookthrough(r, c - 1)
            lookthrough(r, c + 1)

        for r in range(rows):
            lookthrough(r, 0)
            lookthrough(r, cols - 1)
        for c in range(cols):
            lookthrough(0, c)
            lookthrough(rows - 1, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "S":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"