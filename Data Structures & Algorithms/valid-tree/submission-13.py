class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edgeDict = {i : [] for i in range(n)}
        for node, edge in edges:
            edgeDict[node].append(edge)
            edgeDict[edge].append(node)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for neighbor in edgeDict[node]:
                if neighbor == parent:
                    continue

                if not dfs(neighbor, node):
                    return False

            return True

        res = dfs(0, -1)
        if len(visited) == n and res:
            return True

        return False