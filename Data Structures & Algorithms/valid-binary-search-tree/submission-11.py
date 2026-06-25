# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque()
        q.append((root, float("-inf"), float("+inf")))

        while q:
            curr, left, right = q.popleft()

            if not (left < curr.val < right):
                return False

            if curr.left:
                q.append((curr.left, left, curr.val))

            if curr.right:
                q.append((curr.right, curr.val, right))

        return True 
            
