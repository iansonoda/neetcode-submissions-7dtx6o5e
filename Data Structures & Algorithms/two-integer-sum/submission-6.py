class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in hashset:
                return [hashset[complement], i]

            hashset[num] = i