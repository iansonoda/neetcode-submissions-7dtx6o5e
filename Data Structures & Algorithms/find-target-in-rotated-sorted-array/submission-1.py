class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        res = -1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            elif nums[m] >= nums[l]: # Left side is sorted
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            else: # Right side sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return res
