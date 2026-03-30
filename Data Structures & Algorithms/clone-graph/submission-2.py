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

        new = {}
        new[node] = Node(node.val)
        q = deque()
        q.append(node)


        while q:
            curr = q.popleft()
            for neighbor in curr.neighbors:
                # check if in the new graph:
                if neighbor not in new:
                    new[neighbor] = Node(neighbor.val)
                    q.append(neighbor)

                new[curr].neighbors.append(new[neighbor])
                
        return new[node]

        