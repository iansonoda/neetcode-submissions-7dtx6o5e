"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        copied = {}
        copied[node] = Node(node.val)

        q = deque()
        q.append(node)

        while q:
            curr = q.popleft()

            for neighbor in curr.neighbors:
                if neighbor not in copied:
                    copied[neighbor] = Node(neighbor.val)
                    q.append(neighbor)

                copied[curr].neighbors.append(copied[neighbor])

        return copied[node]
        # BFS