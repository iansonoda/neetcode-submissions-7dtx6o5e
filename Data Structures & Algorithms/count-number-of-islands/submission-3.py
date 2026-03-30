class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        if not grid: 
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = dr + row, dc + col
                    if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0"):
                            continue

                    q.append((r, c))
                    grid[r][c] = "0"

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    bfs(i, j)
                    islands += 1


        return islands

        
        