class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjlist = [[] for _ in range(n)]

        for u, v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for neighbor in adjlist[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n
