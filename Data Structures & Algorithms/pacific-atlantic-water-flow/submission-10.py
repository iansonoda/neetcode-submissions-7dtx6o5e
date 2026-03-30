class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        inPacific = set()
        inAtlantic = set()

        def dfs(r, c, visited, lastHeight):
            if ((r, c) in visited or
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                heights[r][c] < lastHeight):

                return

            # We know this is a valid square
            visited.add((r, c))

            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(COLS):
            dfs(0, c, inPacific, heights[0][c])
            dfs(ROWS - 1, c, inAtlantic, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, inPacific, heights[r][0])
            dfs(r, COLS - 1, inAtlantic, heights[r][COLS - 1])

        sol = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in inPacific and (r,c) in inAtlantic:
                    sol.append([r, c])

        return sol
