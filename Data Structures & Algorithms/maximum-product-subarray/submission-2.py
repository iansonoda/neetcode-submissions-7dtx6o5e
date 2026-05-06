class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin, curMax = 1, 1

        res = max(nums)

        for num in nums:
            tmp = num * curMax
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(tmp, num * curMin, num)
            res = max(res, curMax)

        return res