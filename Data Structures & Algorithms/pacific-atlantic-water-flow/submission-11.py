class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        inPacific = set()
        inAtlantic = set()
        ROWS, COLS = len(heights), len(heights[0])
        
        def dfs(r, c, visited, lastHeight):
            if (r not in range(ROWS) or c not in range(COLS)
                or (r, c) in visited or heights[r][c] < lastHeight):

                return

            visited.add((r,c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])


        for r in range(ROWS):
            dfs(r, 0, inPacific, heights[r][0])
            dfs(r, COLS - 1, inAtlantic, heights[r][COLS - 1])

        for c in range(COLS):
            dfs(0, c, inPacific, heights[0][c])
            dfs(ROWS - 1, c, inAtlantic, heights[ROWS - 1][c])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in inAtlantic and (r,c) in inPacific:
                    res.append([r,c])

        return res
            