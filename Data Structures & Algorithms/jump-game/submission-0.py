class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curGoal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if curGoal - i <= nums[i]:
                curGoal = i

        return curGoal == 0