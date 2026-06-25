# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = collections.deque()
        q.append((root, root.val))

        res = 0

        while q:
            curr, maxval = q.popleft()

            if curr.val >= maxval:
                res += 1

            if curr.left:
                q.append((curr.left, max(curr.val, maxval)))

            if curr.right:
                q.append((curr.right, max(curr.val, maxval)))

        return res




