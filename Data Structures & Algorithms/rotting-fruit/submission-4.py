class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        dist = 0
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))

                if grid[r][c] == 1:
                    fresh += 1

        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in dirs:
                    r, c = dr + row, dc + col

                    if (r in range(ROWS) and c in range(COLS) and grid[r][c] == 1):
                        q.append((r, c))
                        grid[r][c] = 0
                        fresh -= 1

            dist += 1

        if fresh > 0:
            return -1

        return dist

        



