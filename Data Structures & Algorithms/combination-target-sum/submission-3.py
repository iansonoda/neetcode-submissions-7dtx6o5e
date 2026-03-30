class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        
        def dfs(i, curr, total):
            # Base case
            if total == target:
                # Don't want to add the actual ref to it
                res.append(curr.copy())
                return

            # Impossible
            if i >= len(nums) or total > target:
                return

            # Left decision tree
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])

            # Remove nums[i] from tree (cleaning) before right:
            # Never including this candidate in the decision tree
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res

            