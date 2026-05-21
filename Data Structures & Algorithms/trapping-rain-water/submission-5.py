class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxl = height[l]
        maxr = height[r]
        res = 0
        curr_i = 0

        while l < r:
            max_water = min(maxl, maxr) - height[curr_i]
            if max_water > 0:
                res += max_water

            if maxl <= maxr:
                l += 1
                maxl = max(maxl, height[l])
                curr_i = l

            elif maxr < maxl:
                r -= 1
                maxr = max(maxr, height[r])
                curr_i = r

        return res