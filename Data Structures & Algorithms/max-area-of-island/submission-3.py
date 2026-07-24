class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        visited = set()
        max_area = 0
        ROWS, COLS = len(grid), len(grid[0])

        if not grid:
            return 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            res = 1

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if r in range(ROWS) and c in range(COLS) and grid[r][c] == 1 and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))
                        res += 1

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and ((r, c)) not in visited:
                    max_area = max(max_area, bfs(r, c))

        return max_area

