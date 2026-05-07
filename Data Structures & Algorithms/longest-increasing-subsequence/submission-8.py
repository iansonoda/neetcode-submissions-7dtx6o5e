class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lengths = [1] * len(nums)

        for i in range(1, len(nums)):
            subproblems = [lengths[k] for k in range(i) if nums[k] < nums[i]]
            if len(subproblems) > 0:
                m = subproblems[0]
                for length in subproblems:
                    if length > m:
                        m = length
                lengths[i] = 1 + m    

        return max(lengths)
        