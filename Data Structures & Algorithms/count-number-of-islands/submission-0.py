class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        rows = len(grid)
        cols = len(grid[0])

        def find_island(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != "1":
                return

            grid[r][c] = "0"

            find_island(r + 1, c)
            find_island(r - 1, c)
            find_island(r, c - 1)
            find_island(r, c + 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    find_island(r, c)
        
        return islands
