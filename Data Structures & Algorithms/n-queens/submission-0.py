class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        solutions = []
        # Store the column index for each row. 
        # index = row, value = col
        board = [-1] * n 
        
        # Look-up sets to track under-attack paths in O(1) time
        cols = set()
        pos_diag = set()  # (row + col)
        neg_diag = set()  # (row - col)
        
        def backtrack(row: int):
            # Base Case: All queens successfully placed
            if row == n:
                solutions.append(format_board(board))
                return
            
            for col in range(n):
                # If the square is under attack, skip it
                if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                    continue
                
                # 1. Place the queen (Make decision)
                board[row] = col
                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)
                
                # 2. Recurse to the next row
                backtrack(row + 1)
                
                # 3. Remove the queen (Backtrack)
                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)
                
        def format_board(board_state):
            formatted = []
            for col_idx in board_state:
                row_str = ["."] * n
                row_str[col_idx] = "Q"
                formatted.append("".join(row_str))
            return formatted

        backtrack(0)
        return solutions
