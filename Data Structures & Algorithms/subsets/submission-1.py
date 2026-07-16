class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        curr = []

        def dfs(i):
            if i >= len(nums):
                res.append(curr.copy())
                return

            # Left
            curr.append(nums[i])
            dfs(i + 1)

            # Right
            curr.pop()
            dfs(i + 1)

        dfs(0)

        return res